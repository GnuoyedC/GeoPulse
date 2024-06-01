from geopulse.gdelt.gdelt_api.config.config import Config as cfg
from geopulse.gdelt.gdelt_api.utils.params_util import ParamsUtils as paramsutil
class UrlUtils:
    BASE_URL = "https://api.gdeltproject.org/api/v2"

    @classmethod
    def construct_default_url(cls):
        default_params_list = paramsutil.set_default_params()
        print(default_params_list, " is the default params list")
        print(cls.BASE_URL, ' is the base url')
        print(paramsutil.API_TYPE_PARAMS.get('geo','default'), ' is the default for geo')
        return cls.construct_url(cls.BASE_URL,paramsutil.API_TYPE_PARAMS.get('geo','defaultapitype'),default_params_list)
    @classmethod
    def construct_url(cls,base_url:str,api_type:str,params_list:list):
        url = '/'.join([base_url,api_type])
        if len(params_list) > 0:
            params = paramsutil.construct_params(params_list)
            url = (''.join([url,paramsutil.QUERY_STEM,params]))
        return url
