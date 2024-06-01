from typing import Any
from common.common_warnings import common_warnings
import os
import sys
# Add the parent directory of the current file to sys.path
class FileHandler:
    @classmethod
    def get_filepath_directory(cls,file_path:str) -> Any:
        if os.path.isfile(file_path):
            return os.path.dirname(os.path.abspath(file_path))
    @classmethod
    def get_dir_files(cls,dir_path,with_extension=None):
        if not os.path.isdir(dir_path):
            common_warnings.ShowWarning('DIR_NOT_EXISTS')
        file_list = [file for file in os.listdir(dir_path) if with_extension and file.endswith(with_extension)]
        if not len(file_list) > 0:
            file_list = [file for file in os.listdir(dir_path)]

        return [os.path.join(dir_path,file) for file in file_list]
