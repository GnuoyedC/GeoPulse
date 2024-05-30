import os
import glob
from typing import Dict, Any
from common.json_handler import JsonHandler as jsh
from common.file_handler import FileHandler as fh

class ConfigHandler:
    CURRENT_DIRECTORY = fh.get_filepath_directory(__file__)
    CONF_FILETYPE = "json"
    CONFIG_FILES = [os.path.splitext(os.path.basename(x))[0] for x in glob.glob(os.path.join(CURRENT_DIRECTORY, f"*.{CONF_FILETYPE}"))]
    VIEW_DIR_ERR = "Cannot view current directory path."
    CONF_TYP_ERR = "Config type not passed."

    @classmethod
    def get_config_file(cls, config_name: str) -> Dict[str, Any]:
        """
        Get the configuration from the specified config file.

        Args:
            config_name (str): The name of the configuration file without extension.

        Returns:
            dict: The configuration data.

        Raises:
            ValueError: If CURRENT_DIRECTORY or config_name is not set.
            FileNotFoundError: If the specified configuration file does not exist.
        """
        if not cls.CURRENT_DIRECTORY:
            raise ValueError(cls.VIEW_DIR_ERR)
        if not config_name:
            raise ValueError(cls.CONF_TYP_ERR)

        config_file_path = os.path.join(cls.CURRENT_DIRECTORY, f"{config_name}.{cls.CONF_FILETYPE}")
        if os.path.exists(config_file_path):
            return jsh.get_json_from_file(config_file_path)
        raise FileNotFoundError(f"The configuration file '{config_name}.{cls.CONF_FILETYPE}' was not found in the directory.")

    @classmethod
    def get_params_config(cls) -> Dict[str, Any]:
        """
        Get the parameters configuration from 'params.json'.

        Returns:
            dict: The parameters configuration.
        """
        return cls.get_config_file("params")

    @classmethod
    def get_themes_config(cls) -> Dict[str, Any]:
        """
        Get the themes configuration from 'key_themes.json'.

        Returns:
            dict: The themes configuration.
        """
        return cls.get_config_file("themes")

if __name__ == '__main__':
    params_config = ConfigHandler.get_params_config()
    print(params_config)
    themes_config = ConfigHandler.get_themes_config()
    print(themes_config)

