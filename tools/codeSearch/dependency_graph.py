### Requirements
1. **Python**: Ensure Python is installed on your system.
2. **Graphviz**: Install both the Graphviz Python library and the Graphviz software.
   - Python library: `pip install graphviz`
   - Graphviz software: Download and install from [Graphviz's website](https://graphviz.org/download/).

### PoC Script: `dependency_visualizer.py`

```python
import os
import ast
from graphviz import Digraph

class DependencyGrapher(ast.NodeVisitor):
    def __init__(self):
        self.imports = set()

    def visit_Import(self, node):
        for alias in node.names:
            self.imports.add(alias.name)
    
    def visit_ImportFrom(self, node):
        self.imports.add(node.module)

def extract_imports(file_path):
    with open(file_path, 'r') as file:
        root = ast.parse(file.read(), filename=file_path)
    grapher = DependencyGrapher()
    grapher.visit(root)
    return grapher.imports

def create_dependency_graph(directory):
    graph = Digraph(comment='Dependency Graph', format='png')
    files = [f for f in os.listdir(directory) if f.endswith('.py')]

    for file in files:
        file_path = os.path.join(directory, file)
        imports = extract_imports(file_path)
        for imp in imports:
            graph.edge(file, imp + '.py')

    return graph

# Directory containing Python files
directory_path = 'path_to_your_python_files'
graph = create_dependency_graph(directory_path)
graph.render('dependency-graph', view=True)
```

### How to Use
1. Replace `'path_to_your_python_files'` with the path to the directory containing your Python files.
2. Run the script. It will generate a PNG file named `dependency-graph.png` showing the dependency graph.

