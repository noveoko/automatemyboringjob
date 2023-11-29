python
import ast
import os

class VariableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.variables.add(node.id)

def find_python_files(directory, ignore_dirs):
    for root, dirs, files in os.walk(directory):
        # Modify the dirs list in-place to skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if file.endswith('.py'):
                yield os.path.join(root, file)

def extract_variables_from_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    tree = ast.parse(file_content)
    visitor = VariableVisitor()
    visitor.visit(tree)
    return visitor.variables

def main(directory, ignore_dirs):
    all_variables = set()
    for file_path in find_python_files(directory, ignore_dirs):
        variables = extract_variables_from_file(file_path)
        all_variables.update(variables)
    return all_variables

# Replace 'your_project_directory' with the path to your Python project directory
project_directory = 'your_project_directory'
ignore_dirs = ['dir_to_ignore1', 'dir_to_ignore2']  # Replace with directories to ignore
variables = main(project_directory, ignore_dirs)
print(variables)