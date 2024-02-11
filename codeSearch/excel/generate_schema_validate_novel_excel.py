from typing import Dict, Any, Type
from pydantic import BaseModel,create_model
import pandas as pd
import datetime


def pandas_type_to_python_type(dtype_name: str) -> Type:
    mapping = {
        'int64': int,
        'float64': float,
        'bool': bool,
        'datetime64[ns]': datetime.datetime,
        'timedelta[ns]': datetime.timedelta,
        # add more if needed
    }
    return mapping.get(dtype_name, str)  # default to str if no match

def generate_pydantic_schema(excel_file: str) -> BaseModel:
    # Read the Excel file
    xls = pd.ExcelFile(excel_file)

    # Get the sheet names
    sheet_names = xls.sheet_names

    # Initialize an empty dictionary to hold the schemas
    schemas: Dict[str, Any] = {}

    # Loop over each sheet
    for sheet_name in sheet_names:
        # Read the sheet into a DataFrame
        df = xls.parse(sheet_name)

        # Get the column names and types
        columns = {col: (pandas_type_to_python_type(df[col].dtype.name), ...) for col in df.columns}

        # Create a Pydantic model for the sheet
        schemas[sheet_name] = create_model(sheet_name, **columns)

    return schemas


def validate_excel_file(excel_file: str, schema: Type[BaseModel]):
    # Read the Excel file
    xls = pd.ExcelFile(excel_file)

    # Get the sheet names
    sheet_names = xls.sheet_names

    # Loop over each sheet
    for sheet_name in sheet_names:
        # Read the sheet into a DataFrame
        df = xls.parse(sheet_name)

        # Convert the DataFrame into a dictionary
        data = df.to_dict(orient='records')

        # Validate the data using the Pydantic schema
        for row in data:
            model_instance = schema(**row)

        print(f"Data in sheet {sheet_name} is valid!")


excel_input = r"C:\Users\mrkra\Downloads\titanic3.xls"
schema = generate_pydantic_schema(excel_input)

validate_excel_file(excel_input, schema['titanic3'])
