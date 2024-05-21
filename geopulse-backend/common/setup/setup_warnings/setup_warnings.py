import warnings
SETUP_EXISTS = 'SETUP_EXISTS'

WARNING_MESSAGES = { 
    SETUP_EXISTS: "Setup already exists.",
}

def ShowWarning(warning_type:str) -> None:
    if warning_type in WARNING_MESSAGES:
        warnings.warn(WARNING_MESSAGES[warning_type])
    else:
        warnings.warn('Unknown warning types: {}'.format(warning_type))
