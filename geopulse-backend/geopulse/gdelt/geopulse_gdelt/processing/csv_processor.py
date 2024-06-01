import argparse
import pandas as pd
import common.model_helper as modelhelper
from geopulse.gdelt.geopulse_gdelt.config.config import Config as cfg
from geopulse.events_data.models import GeoFlashpointRisk
fields = modelhelper.get_model_fields(GeoFlashpointRisk)

def csv_to_dataframe(file_path:str, columns=[],delimiter='\t'):
    """
    Convert a CSV file without headers to a Pandas DataFrame and assign column names.

    Parameters:
        - file_path: str, path to the CSV file.
        - column_names: list of str, list of column names to assign.

    Returns:
        - df: Pandas DataFrame with assigned column names.
    """
    # Read the CSV file without headers
    df = pd.read_csv(file_path, header=None,sep=delimiter)
    # Check if the number of columns in the CSV matches the number of column names provided
    if len(df.columns) != len(columns):
        raise ValueError("The number of columns in the CSV does not match the number of column names provided.")

    # Assign the column names
    df.columns = columns 

    return df

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Process GDELT CSV files.")
    parser.add_argument('csv_path', type=str, help="The path to the GDELT CSV file.")
    parser.add_argument('csv_dir', type=str, nargs='+', help="The directory of the GDELT CSV files.")
