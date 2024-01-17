from pydantic import BaseModel
import pandas as pd

class ExcelData(BaseModel):
    column1: int
    column2: str
    column3: float

def validate_excel(file_path):
    # Load Excel file into a DataFrame
    df = pd.read_excel(file_path)

    # Iterate through rows and validate using Pydantic
    for index, row in df.iterrows():
        excel_data = ExcelData(**row)
        excel_data.dict()

    return "Validation successful!"

# Replace 'your_excel_file.xlsx' with the actual path to your Excel file
file_path = 'your_excel_file.xlsx'
result = validate_excel(file_path)
print(result)
