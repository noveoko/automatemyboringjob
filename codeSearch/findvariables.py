To extract all variable names from a Python project, you will first need to parse the Python code files. This can be done using the `ast` module (Abstract Syntax Trees) in Python, which can analyze and interpret the structure of Python code.

Here's a Python script that can do this:

1. It will search through all Python files in a given directory.
2. It will parse each file to find all the variable names.

This script assumes that you have a folder structure where all your Python files are in a single directory or its subdirectories.

```python
import ast
import os

class VariableVisitor(ast.NodeVisitor):
    def __init__(self):
        self.variables = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.variables.add(node.id)

def find_python_files(directory):
    for root, dirs, files in os.walk(directory):
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

def main(directory):
    all_variables = set()
    for file_path in find_python_files(directory):
        variables = extract_variables_from_file(file_path)
        all_variables.update(variables)
    return all_variables

# Replace 'your_project_directory' with the path to your Python project directory
project_directory = 'your_project_directory'
variables = main(project_directory)
print(variables)
```

Remember to replace `'your_project_directory'` with the actual path to your project directory. This script will print all the variable names used in your Python project.

Keep in mind that this script identifies variable names based on the `ast.Store` context, which means it catches variables that are being assigned values. It may not catch every possible usage of a variable (like in global statements or as function arguments).