# preprocessor.py
import pandas as pd

def load_data(file_path):
    """Loads the dataset and performs basic cleaning."""
    try:
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip()  # Remove any leading/trailing spaces in column names
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def filter_data(data, year=None, state=None):
    """Filters the dataset based on selected year and/or state."""
    if year:
        data = data[data['YEAR'] == year]
    if state:
        data = data[data['State/UT'] == state]
    return data


