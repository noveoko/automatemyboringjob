python
import pandas as pd

# Specify the file path of your Excel workbook
excel_file_path = 'your_file.xlsx'

# Use pandas to read a chunk of rows from each sheet
chunk_size = 5  # Adjust the chunk size as needed

xls = pd.ExcelFile(excel_file_path)
column_names = {}

for sheet_name in xls.sheet_names:
    # Read a chunk of rows
    df_chunk = pd.read_excel(excel_file_path, sheet_name=sheet_name, nrows=chunk_size)

    # Fetch column names
    sheet_columns = df_chunk.columns.tolist()
    
    # Store column names in a dictionary
    column_names[sheet_name] = sheet_columns

# Display the column names for each sheet
for sheet_name, columns in column_names.items():
    print(f"Sheet '{sheet_name}': {columns}")
