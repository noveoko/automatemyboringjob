### Requirements
1. **Python**: Ensure Python is installed on your system.
2. **NetworkX and Matplotlib**: Install these Python libraries.
   - Install command: `pip install networkx matplotlib`

### PoC Script: `dependency_visualizer_networkx.py`

```python
import os
import ast
import networkx as nx
import matplotlib.pyplot as plt

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
    G = nx.DiGraph()
    files = [f for f in os.listdir(directory) if f.endswith('.py')]

    for file in files:
        file_path = os.path.join(directory, file)
        imports = extract_imports(file_path)
        for imp in imports:
            G.add_edge(file, imp + '.py')

    return G

def draw_graph(G):
    plt.figure(figsize=(12, 8))
    nx.draw(G, with_labels=True, node_color='lightblue', font_size=8, font_weight='bold', node_size=5000, edge_color='gray')
    plt.title('Dependency Graph')
    plt.show()

# Directory containing Python files
directory_path = 'path_to_your_python_files'
graph = create_dependency_graph(directory_path)
draw_graph(graph)
```

### How to Use
1. Replace `'path_to_your_python_files'` with the path to your Python files directory.
2. Run the script. It will display the dependency graph using `matplotlib`.
