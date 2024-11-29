# AutoCloth for Blender

This updated script includes the following changes and improvements:

1. Support for all cloth properties in Blender 4.0, including main cloth settings, collision settings, and internal springs settings.

2. Separate methods for applying each group of settings (`apply_cloth_settings`, `apply_collision_settings`, `apply_internal_springs_settings`).

3. A more flexible `apply_settings` method that can handle different groups of properties.

4. Updated `create_cloth_preset` method that writes all cloth settings, collision settings, and internal springs settings to the preset file.

5. Better error handling and reporting.

To use this script with your JSON file, make sure your JSON structure matches the expected format. Here's an example of how your JSON file should be structured:

```json
{
  "cloth": {
    "quality": 5,
    "mass": 0.3,
    "bending_stiffness": 0.5,
    "tension_stiffness": 15,
    "compression_stiffness": 15,
    "shear_stiffness": 5,
    "collision": {
      "use_collision": true,
      "distance_min": 0.015,
      "friction": 0.5
    },
    "internal_springs": {
      "internal_spring_max_length": 0.1,
      "internal_tension_stiffness": 15
    }
  }
}
```

This script should now support all cloth properties available in Blender 4.0. If you encounter any issues or if there are specific properties you need that aren't included, please let me know and I'll be happy to help further.