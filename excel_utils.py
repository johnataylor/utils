import pandas as pd

def read_excel_contents(file_path, sheet_name=0):
    """
    Reads the contents of an Excel file and returns a DataFrame.
    
    :param file_path: Path to the Excel file.
    :param sheet_name: Sheet name or index (default is first sheet).
    :return: pandas DataFrame with the sheet contents.
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    return df