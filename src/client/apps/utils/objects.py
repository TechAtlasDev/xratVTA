import json

class payload:
    def __init__(self, data):
        self.code:str = data.get("code")
        self.reps:int = data.get("reps")
        self.executor:executor = executor(data.get("executor"))
    
    def __str__(self):
        objeto = json.dumps({"code": self.code, "reps": self.reps, "executor": self.executor})
        return objeto

class executor:
    def __init__(self, data):
        self.name:str = data.get("name")
        self.code:int = data.get("code")
        self.execution:str = data.get("execution")
        self.description:str = data.get("description")
        self.postdata:dict = data.get("postdata")