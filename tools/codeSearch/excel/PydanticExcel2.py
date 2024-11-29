import pandas as pd
from pydantic import BaseModel, ValidationError, conlist

# Pydantic model for expected column names
class ExpectedColumns(BaseModel):
    column1: str
    column2: str
    column3: str

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

    # Pydantic validation for column names
    try:
        ExpectedColumns(**{col: col for col in sheet_columns})
    except ValidationError as e:
        print(f"Validation failed for sheet '{sheet_name}'. Incorrect column names.")
        # You can choose to handle validation failures as needed
    else:
        print(f"Validation passed for sheet '{sheet_name}'.")
    
    # Store column names in a dictionary
    column_names[sheet_name] = sheet_columns

# Display the column names for each sheet
for sheet_name, columns in column_names.items():
    print(f"Sheet '{sheet_name}': {columns}")
