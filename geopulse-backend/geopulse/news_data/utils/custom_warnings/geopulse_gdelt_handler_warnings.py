import warnings

# Define warning types
NEWS_EXISTS = 'NEWS_EXISTS'

# Define a mapping of warning types to messages
WARNING_MESSAGES = {
    NEWS_EXISTS: 'A news item with this ID already exists.',
}

def ShowWarning(warning_type:str) -> None:
    if warning_type in WARNING_MESSAGES:
        warnings.warn(WARNING_MESSAGES[warning_type])
    else:
        warnings.warn('Unknown warning type: {}'.format(warning_type))
