from typing import Any
import os
import sys
# Add the parent directory of the current file to sys.path
class FileHandler:
    @classmethod
    def get_filepath_directory(cls,file_path:str) -> Any:
        if os.path.exists(file_path):
            return os.path.dirname(os.path.abspath(file_path))
