import json

class payload:
    def __init__(self, data):
        self.code:str = data.get("code")
        self.reps:int = data.get("reps")
        self.executor:executor = executor(data.get("executor"))

        self.__data__ = data
    
    def __str__(self):
        return self.__data__.__str__()

class executor:
    def __init__(self, data):
        self.name:str = data.get("name")
        self.code:int = data.get("code")
        self.execution:str = data.get("execution")
        self.description:str = data.get("description")
        self.postdata:dict = data.get("postdata", {})
    
        self.__data__ = data

    def __str__(self):
        return self.__data__.__str__()