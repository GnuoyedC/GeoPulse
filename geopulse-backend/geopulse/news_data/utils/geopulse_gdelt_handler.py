import sys
from pathlib import Path
"""
    Handles the logic of getting data from
    the GDELT 2.0 API and transferring it
    to the database.
"""
from gdelt_api_handler import GDELTAPI as api

class GeopulseGDELTHandler:
    @classmethod
    def check_if_exists(cls,item=None):
        if not item:
            print("You must enter an item. Exiting process.")

if __name__ == '__main__':
    GeopulseGDELTHandler.check_if_exists()
