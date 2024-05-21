class NoJsonUrlProvided(Exception):
    def __init__(self,message = "No JSON URL provided."):
        self.message = message
        super().__init__(message)

class NoJsonPathProvided(Exception):
    def __init__(self,message = "No JSON Path provided."):
        self.message = message
        super().__init__(message)
class JsonFileReadError(Exception):
    def __init__(self,message = "JSON file read error"):
        self.message = message
        super().__init__(message)
class JsonResponseError(Exception):
    def __init__(self, message = "An error occurred with the JSON request."):
        self.message = message
        super().__init__(message)
