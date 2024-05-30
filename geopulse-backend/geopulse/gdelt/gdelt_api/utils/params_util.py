from geopulse.gdelt.gdelt_api.config.config_handler import ConfigHandler as cfg
class ParamsUtils:
    API_TYPE_PARAMS = cfg.get_params_config()['API_TYPE']
    RESULTS_FORMATS_PARAMS = cfg.get_params_config()['RESULTS_FORMAT']
    PARAMS = cfg.get_params_config()['PARAMS']
    QUERY_STEM = cfg.get_params_config()['QUERY_STEM']
    DEFAULT_PARAMS_DICT = { 
        "sourcelang": "eng",
        "theme": "ARMEDCONFLICT",
        "sourcecountry": "US",
        "mode": "country",
        "timespan": "1w",
        "format": "geojson",
        "tone": "<-5",
        "sortby": "ToneAsc"
    }
    PARAMS_LIST = []
    @classmethod
    def construct_params(cls,params_list: list) -> str:
        if params_list and len(params_list) > 0:
            """
            Constructs the URL parameters for the API request.
            """
            colon_params = [f"{param}{value}" for param, value in params_list if param.endswith(':') or not param.endswith('=')]
            equals_params = [f"{param}{value}" for param, value in params_list if param.endswith('=')]

            # Join colon parameters with '+' and equals parameters with '&'
            joined_colon_params = '+'.join(colon_params)
            joined_equals_params = '&'.join(equals_params)

            # Combine the two groups
            if joined_colon_params and joined_equals_params:
                return f"{joined_colon_params}&{joined_equals_params}"
            elif joined_colon_params:
                return joined_colon_params
            elif joined_equals_params:
                return joined_equals_params
            return ""
        return ""
    @classmethod
    def get_join_type(cls,param_prefix):
        """
            Determines the character to join the parameters together
            with depending on the param-value separator present
            within the param-value string.
            
            Args:
                param_prefix (str): the param identifier (i.e. 'sourcelang:')
            Returns:
                str
        """
        if param_prefix:
            return "+" if ":" in param_prefix else "&"
    @classmethod
    def format_themes_list(cls,theme_list: list) -> str:
        """
            Consumes a list as a parameter and
            formats it for using it in the
            API query.

            Args:
                theme_list (list): The list of themes extracted from the themes.json file
            Returns:
                themes (str): The themes list, converted to a user/API-friendly string.
        """
        themes = []
        if not theme_list:
            themes = cfg.get_themes_config()['ALL']
        themes = "(" + " OR ".join([theme for theme in themes]) + ")"
        return themes
    @classmethod
    def get_param_prefix(cls,param: str) -> str:
        """
            Using the passed parameter, the function
            checks against the class variable PARAMS
            to identify the parameter prefix.
            
            Args:
                param (str): The parameter to check the PARAMS dict against.
            Returns:
                A string containing the prefix.
            Example:
                ParamsUtils.get_param_prefix("sourcelang") -> "sourcelang:"
                ParamsUtils.get_param_prefix() -> "defaultparamprefix"
        """
        return cls.PARAMS.get(param,'defaultparamprefix')
    @classmethod
    def set_param_value(cls,param,value):
        """
            Takes in a parameter name and the value for that
            parameter, and appends the formatted param-value
            pair to the list of parameters for parameter
            construction.

            Args:
                param (str): Parameter to check the PARAMS class
                variable against.
                value (str): The value to set the prefixed parameter
                to.
            Returns:
                A list containing the prefixed parameter-value tuples.
            Example:
                ParamsUtils.set_param_value('sourcelang','eng') -> [('sourcelang:','eng')]
        """
        cls.PARAMS_LIST.append((cls.get_param_prefix(param),value))
    @classmethod
    def set_default_params(cls):
        """
            Constrcuts a parameter string based on the default
            parameters set on this class' initialization.

            Args:
                None
            Returns:
                String containing the formatted parameters.
            Example:
                ParamsUtils.set_default_params() -> "sourcelang:eng+theme:ARMEDCONFLICT+sourcecountry:US+tone<-5&mode=country&timespan=1w&format=geojson"
        """
        cls.PARAMS_LIST = []
        for param,value in cls.DEFAULT_PARAMS_DICT.items():
            cls.set_param_value(param,value)
        return cls.PARAMS_LIST
        
