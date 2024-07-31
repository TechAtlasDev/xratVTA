import traceback

class ExceptionProcessed:
    def __init__(self, data) -> None:
        self.name = data.get("name")
        self.type = data.get("type")
        self.message = data.get("message")
        self.file = data.get("file")
        self.line = data.get("line")
        self.traceback = data.get("traceback")

class handle:
    def __init__(self, exception):
        self.exception = exception

    def ControlException(self) -> ExceptionProcessed:
        Exception = self.exception

        exception_name = type(Exception).__name__
        exception_type = type(Exception)
        tb = traceback.extract_tb(Exception.__traceback__)
        filename = tb[-1].filename
        line_number = tb[-1].lineno
        mensaje_error = str(Exception)

        exceptionProcess = {
            "name": exception_name,
            "type": exception_type,
            "message": mensaje_error,
            "file": filename,
            "line": line_number,
            "traceback": tb
        }

        return ExceptionProcessed(exceptionProcess)
    
    def __str__(self) -> str:
        Exception = self.exception

        exception_name = type(Exception).__name__
        exception_type = type(Exception)
        tb = traceback.extract_tb(Exception.__traceback__)
        filename = tb[-1].filename
        line_number = tb[-1].lineno
        mensaje_error = str(Exception)

        exceptionProcess = {
            "name": exception_name,
            "type": exception_type,
            "message": mensaje_error,
            "file": filename,
            "line": line_number,
            "traceback": tb
        }

        return exceptionProcess.__str__()