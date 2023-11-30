import os
import re

def find_dataframe_columns(directory):
    column_names = set()

    # Regular expression patterns to find dataframe column assignments
    patterns = [
        r"pd\.DataFrame\([^)]*columns\s*=\s*\[([^\]]+)\]",  # pd.DataFrame with columns
        r"\.columns\s*=\s*\[([^\]]+)\]",                    # .columns assignment
        r"\.rename\s*\([^)]*columns\s*=\s*\{([^\}]+)\}",    # .rename with columns
    ]

    # Traverse the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                
                # Read the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Search for patterns in file content
                    for pattern in patterns:
                        for match in re.finditer(pattern, content):
                            columns_str = match.group(1)
                            
                            # Process and add found column names
                            for col_name in columns_str.split(','):
                                col_name = col_name.strip().strip("'").strip('"')
                                column_names.add(col_name)

    return list(column_names)

# Usage
directory = 'path/to/directory'
columns = find_dataframe_columns(directory)
print(columns)
