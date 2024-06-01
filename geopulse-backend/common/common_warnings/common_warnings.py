import warnings

# Define warning types
DIR_NOT_EXISTS = 'DIR_NOT_EXISTS'
# Define a mapping of warning types to messages
WARNING_MESSAGES = {
    DIR_NOT_EXISTS: 'Provided directory does not exist.',
}

def ShowWarning(warning_type:str) -> None:
    if warning_type in WARNING_MESSAGES:
        warnings.warn(WARNING_MESSAGES[warning_type])
    else:
        warnings.warn('Unknown warning type: {}'.format(warning_type))
