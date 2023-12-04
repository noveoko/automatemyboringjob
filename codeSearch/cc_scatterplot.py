To create a color-coded scatter plot representing the code quality output from the `radon cc` command in Python, we'll need to:

1. Parse the output of the `radon cc` command.
2. Assign color codes based on the quality ratings (e.g., A, B, C, etc.).
3. Create a scatter plot using a library like matplotlib.

Assuming that the `radon cc` command outputs data in a consistent format, here is a Python script that does this:

```python
import matplotlib.pyplot as plt
import re

# Example output from `radon cc` command
radon_output = """
    file1.py
        F 2:0 function1 - A
        F 15:0 function2 - B

    file2.py
        F 8:0 function3 - C
        F 30:0 function4 - D
"""

# Parse the radon output
def parse_radon_output(output):
    pattern = r"F (\d+):\d+ (.+?) - ([A-F])"
    matches = re.findall(pattern, output)
    return [(int(line), name.strip(), grade) for line, name, grade in matches]

# Assign colors based on grade
def get_color(grade):
    colors = {'A': 'green', 'B': 'blue', 'C': 'yellow', 'D': 'orange', 'E': 'red', 'F': 'purple'}
    return colors.get(grade, 'gray')

# Create scatter plot
def create_scatter_plot(data):
    x = [item[0] for item in data]  # Line numbers
    y = range(len(data))  # Just to spread the points vertically
    colors = [get_color(item[2]) for item in data]  # Grade colors

    plt.scatter(x, y, c=colors)
    for i, txt in enumerate(data):
        plt.annotate(txt[1], (x[i], y[i]))
    plt.xlabel('Line Number')
    plt.ylabel('Functions')
    plt.title('Code Quality Scatter Plot')
    plt.show()

# Parse the output and create the plot
data = parse_radon_output(radon_output)
create_scatter_plot(data)
```

This script assumes that the `radon cc` output is stored in the `radon_output` string variable. You will need to replace this with the actual output from your `radon cc` command. The script parses the output, assigns colors based on the grades, and then creates a scatter plot where each point represents a function, its position on the X-axis indicates the line number, and the color indicates the code quality grade.

Please make sure you have matplotlib installed (`pip install matplotlib`) to run this script. Also, adjust the parsing logic if your `radon cc` output format is different.