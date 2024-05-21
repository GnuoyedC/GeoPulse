import requests
import json
from exceptions.json_handler_exceptions import (
    NoJsonUrlProvided,
    JsonResponseError
)
from typing import Dict,Any
class JsonHandler:
    """
        Handles all json-related functionality
        within this app.
    """
    headers = { 'Content-Type': 'application/json' }
    @classmethod
    def get_json_from_url(cls, url:str) -> Dict[str,Any]:
        if not url:
            raise NoJsonUrlProvided
        try:
            response = requests.get(url)
            return response.json()
        except:
            raise JsonResponseError
    @classmethod
    def get_json_from_file(cls, json_path:str) -> Dict[str,Any]:
        if not json_path:
            raise
        try:
            with open(json_path) as json_file:
                json_data = json.load(json_file)
                return json_data
        except:
            raise
