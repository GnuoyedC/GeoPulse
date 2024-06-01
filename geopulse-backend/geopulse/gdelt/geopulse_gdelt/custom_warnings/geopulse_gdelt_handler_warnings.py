import warnings

# Define warning types
EVENT_EXISTS = 'EVENT_EXISTS'
# Define a mapping of warning types to messages
WARNING_MESSAGES = {
    EVENT_EXISTS: 'An event item with this ID already exists.',
}

def ShowWarning(warning_type:str) -> None:
    if warning_type in WARNING_MESSAGES:
        warnings.warn(WARNING_MESSAGES[warning_type])
    else:
        warnings.warn('Unknown warning type: {}'.format(warning_type))
