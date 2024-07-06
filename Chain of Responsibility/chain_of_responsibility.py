from abc import ABC, abstractmethod

class HttpRequest:
    
    def __init__(self, username, password) -> None:
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, name):
        self._username = name

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, code):
        self._password = code      

class Handler(ABC):

    def __init__(self, next:"Handler") -> None:
        self.next = next
    
    @abstractmethod
    def do_handle(self):
        pass

    def handle(self, request:HttpRequest):
        if self.do_handle(request):
            return
        
        if self.next:
            self.next.handle(request)

class Authenticator(Handler):

    def __init__(self, next: Handler) -> None:
        super().__init__(next)
    
    def do_handle(self, request:HttpRequest):
        is_valid = (request.username == "admin" and 
                   request.password == "1234")
        print("Authentication")
        return not is_valid

class Compressor(Handler):

    def __init__(self, next: Handler) -> None:
        super().__init__(next)
    
    def do_handle(self, request:HttpRequest):
        print("Compress")
        return False

class Logger(Handler):

    def __init__(self, next: Handler) -> None:
        super().__init__(next)
    
    def do_handle(self, request:HttpRequest):
        print("Log")
        return False

class WebServer:
    def __init__(self, handler:Handler) -> None:
        self.handler = handler

    def handle(self, request:HttpRequest):
        self.handler.handle(request)

# Authenticator --> Logger --> Compressor
compressor = Compressor(None)
logger=Logger(compressor)
authenticator = Authenticator(logger)
server = WebServer(authenticator)
http_request = HttpRequest("admin", "1234")
server.handle(http_request)
