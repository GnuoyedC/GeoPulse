from geopulse.gdelt.gdelt_api.config.config_handler import ConfigHandler as cfg
def get_join_type(param_prefix):
    if param_prefix:
        return "+" if ":" in param_prefix else "&"
def format_themes_list(theme_list: list) -> str:
    themes = []
    if not theme_list:
        themes = cfg.get_themes_config()['ALL']
    themes = "(" + " OR ".join([theme for theme in themes]) + ")"
    return themes
