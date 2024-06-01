import pandas as pd
import geopulse.gdelt.geopulse_gdelt.processing.csv_processor as csv
from common.file_handler import FileHandler as files
from geopulse.gdelt.geopulse_gdelt.config.config import Config
from geopulse.events_data.models import GeoFlashpointRisk
import geopulse.events_data.helpers.geoflashpointrisk as gfpr_helper
import geopulse.gdelt.geopulse_gdelt.processing.df_processor as df_processor
"""
    Handles the logic of getting data from
    the GDELT 2.0 API and transferring it
    to the database.
"""

class GeopulseGDELTHandler:
    @classmethod
    def load_config(cls):
        actor_codes = Config.get_codes_config('ACTOR')
        cameo_codes = Config.get_codes_config('CAMEO')
        temp_dir = Config.get_paths_config('TEMP_DIR')
        return actor_codes, cameo_codes, temp_dir
    @classmethod
    def check_if_exists(cls,item=None):
        if not item:
            print("You must enter an item. Exiting process.")
    @classmethod
    def test(cls):
        actor_codes, cameo_codes, temp_dir = cls.load_config()
        CSV_FILES = files.get_dir_files(dir_path=temp_dir,with_extension='.CSV')
        for csv_file in CSV_FILES:

        #csv_file_path = '/tmp/geopulse/20240530140000.export.CSV'
        #print(f"Loading CSV file: {csv_file_path}")
            csv_df = csv.csv_to_dataframe(file_path=csv_file, columns=gfpr_helper.get_geoflashpointrisk_fields())
        
            # Preprocess the dataframe
            csv_df = df_processor.preprocess_dataframe(csv_df)
            csv_df_filtered = df_processor.filter_dataframe(csv_df,actor_codes,cameo_codes)
            # Combine both masks to filter the DataFrame
            print("Creating new instances...")
            new_instances = [GeoFlashpointRisk(**row.to_dict()) for index, row in csv_df_filtered.iterrows()]
            print(f"Created {len(new_instances)} new instances of GeoFlashpointRisk.")
            if new_instances:
                print(csv_df_filtered.dtypes)
                print("Inserting new instances into the database...")
                GeoFlashpointRisk.objects.bulk_create(new_instances)
                print("Insertion complete.")
        print("Finished test method.")


    @classmethod
    def get_conflict_data(cls) -> pd.DataFrame:
        return pd.DataFrame()

