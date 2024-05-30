# geopulse/gdelt_api/gdelt_api.py
# Add the common directory to sys.path
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from geopulse.gdelt.gdelt_api.utils.params_util import ParamsUtils as paramsutil
class GdeltAPI:
    def __init__(self,):
        self.set_params_list = []
        return
    def get(self,**kwargs):
         for param, value in kwargs.items():
            paramsutil.set_param_value(param, value)
         paramsutil.construct_params(self.set_params_list)
        

if __name__ == '__main__':
    gdelt = GdeltAPI()
    #gdelt.set_param_value("lang","english")
    #gdelt.set_param_value("theme","politics")
    #gdelt.set_param_value("timespan","3d")
