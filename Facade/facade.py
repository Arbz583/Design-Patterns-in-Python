class Message:

    def __init__(self, content) -> None:
        self.content = content

class NotificationServer:
    
    def connect(self, ip_address):
        return Connection()

    def authentication(self, app_id, key:str):
        return AuthToken()

    def send(self, auth_token:"AuthToken", message:Message, target):
        print("Sending a message")

class Connection:

    def disconnect(self):
        pass

class AuthToken:
    pass



class NotificationService:

    def send(self, message:str, target:str):
        server = NotificationServer()
        connection = server.connect(ip_address="1313")
        auth_token = server.authentication(
            app_id="3245",
            key="password"
            )
        message = Message(message)
        server.send(auth_token, message, target=target)
        connection.disconnect()

service = NotificationService()
service.send("hi there", "ali")