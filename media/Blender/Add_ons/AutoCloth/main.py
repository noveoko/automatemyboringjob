import bpy
import json
import os
from bpy_extras.io_utils import ImportHelper
from bpy.types import Operator
from bpy.props import StringProperty

bl_info = {
    "name": "Apply Physics from JSON",
    "blender": (4, 0, 0),
    "category": "Import-Export",
}

class ApplyPhysicsFromJSON(Operator, ImportHelper):
    """Apply Physics from JSON and Create Preset"""
    bl_idname = "import_mesh.apply_physics_from_json"
    bl_label = "Apply Physics from JSON"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = ".json"
    filter_glob: StringProperty(default="*.json", options={'HIDDEN'})

    def execute(self, context):
    try:
        with open(self.filepath, 'r') as file:
            data = json.load(file)
    except Exception as e:
        self.report({'ERROR'}, f"Failed to load JSON file: {e}")
        return {'CANCELLED'}

    obj = context.active_object
    if not obj or obj.type != 'MESH':
        self.report({'ERROR'}, "No active mesh object selected.")
        return {'CANCELLED'}

    # Look for the first key in the JSON data
    cloth_key = next(iter(data))
    if cloth_key:
        cloth_data = data[cloth_key]
        cloth_modifier = next((mod for mod in obj.modifiers if mod.type == 'CLOTH'), None)
        if not cloth_modifier:
            bpy.ops.object.modifier_add(type='CLOTH')
            cloth_modifier = obj.modifiers[-1]

        self.apply_cloth_settings(cloth_modifier.settings, cloth_data)
        self.apply_collision_settings(cloth_modifier.collision_settings, cloth_data.get("collision", {}))
        self.apply_internal_springs_settings(cloth_modifier.internal_springs_settings, cloth_data.get("internal_springs", {}))

        preset_name = os.path.splitext(os.path.basename(self.filepath))[0]
        self.create_cloth_preset(preset_name, cloth_modifier)

        self.report({'INFO'}, f"Physics applied successfully and preset '{preset_name}' created.")
    else:
        self.report({'WARNING'}, "No cloth data found in JSON file.")

    return {'FINISHED'}

    def apply_cloth_settings(self, settings, data):
        properties = [
            "quality", "mass", "air_damping", "bending_model", "bend_stiffness", "bending_stiffness", 
            "compression_damping", "compression_stiffness", "density_target", "density_strength", 
            "internal_compression_stiffness", "internal_tension_stiffness", "pin_stiffness", 
            "shear_damping", "shear_stiffness", "shrink_min", "shrink_max", "tension_damping", 
            "tension_stiffness", "uniform_pressure_force", "use_dynamic_mesh", "use_pressure", 
            "use_internal_springs", "vertex_group_mass", "vertex_group_pressure", "vertex_group_shrink"
        ]
        self.apply_settings(settings, data, properties)

    def apply_collision_settings(self, settings, data):
        properties = [
            "collision_quality", "distance_min", "friction", "damping", "thickness_outer", 
            "thickness_inner", "use_collision", "use_self_collision", "self_friction", 
            "self_distance_min", "self_impulse_clamp"
        ]
        self.apply_settings(settings, data, properties)

    def apply_internal_springs_settings(self, settings, data):
        properties = [
            "internal_spring_max_diversion", "internal_spring_max_length", "internal_spring_normal_check", 
            "internal_tension_stiffness", "internal_compression_stiffness", "internal_springs_vertex_group"
        ]
        self.apply_settings(settings, data, properties)

    def apply_settings(self, settings, data, properties):
        for prop in properties:
            if prop in data:
                setattr(settings, prop, data[prop])

    def create_cloth_preset(self, name, cloth_modifier):
        presets_path = bpy.utils.user_resource('SCRIPTS', path="presets/cloth")
        os.makedirs(presets_path, exist_ok=True)
        preset_file = os.path.join(presets_path, f"{name}.py")
        
        with open(preset_file, 'w') as f:
            f.write("import bpy\n")
            f.write("cloth = bpy.context.object.modifiers.active\n\n")
            
            self.write_settings(f, cloth_modifier.settings, "cloth.settings")
            self.write_settings(f, cloth_modifier.collision_settings, "cloth.collision_settings")
            self.write_settings(f, cloth_modifier.internal_springs_settings, "cloth.internal_springs_settings")

        self.report({'INFO'}, f"Cloth preset '{name}' created at {preset_file}")

    def write_settings(self, file, settings, prefix):
        for prop in dir(settings):
            if not prop.startswith("__") and not callable(getattr(settings, prop)):
                value = getattr(settings, prop)
                file.write(f"{prefix}.{prop} = {repr(value)}\n")
        file.write("\n")

def menu_func_import(self, context):
    self.layout.operator(ApplyPhysicsFromJSON.bl_idname, text="Apply Physics from JSON")

def register():
    bpy.utils.register_class(ApplyPhysicsFromJSON)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ApplyPhysicsFromJSON)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
