import pandas as pd
from tabulate import tabulate
from excel_utils import read_excel_contents

if __name__ == "__main__":
    # Example usage and test
    test_file = "Book1.xlsx"  # Specify the Excel file to read
    try:
        # Read the Excel file into a DataFrame
        df = read_excel_contents(test_file)
        # Capitalize the first letter of each column name
        df.columns = [col.capitalize() for col in df.columns]
        # Print the DataFrame in a formatted table
        # tabulate parameters:
        # headers='keys'      -> use DataFrame column names as table headers
        # tablefmt='psql'     -> use PostgreSQL-style table formatting
        # showindex=False     -> do not display the DataFrame index column
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    except Exception as e:
        # Print an error message if reading fails
        print(f"Error reading Excel file: {e}")

