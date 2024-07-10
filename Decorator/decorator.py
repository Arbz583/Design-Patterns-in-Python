from abc import ABC, abstractmethod

class Stream(ABC):

    @abstractmethod
    def write(self, data):
        pass

class CloudStream(Stream):

    def write(self, data):
        print("Storing", data)

class EncryptCloudStream(Stream):

    def __init__(self, stream:Stream) -> None:
        self.stream = stream

    def write(self, data):
        encrypted_data = self.encrypt(data)
        self.stream.write(encrypted_data)

    def encrypt(self, data):
        return f"^%$^{data}*&^"

class CompressCloudStream(Stream):

    def __init__(self, stream:Stream) -> None:
        self.stream = stream

    def write(self, data):
        compressed_data = self.compress(data)
        self.stream.write(compressed_data)

    def compress(self, data):
        return data[:5]
    

def store_credit_card(stream:Stream):
    stream.write(data="1236-2548-2536-9845")

store_credit_card(EncryptCloudStream
                  (CompressCloudStream
                   (CloudStream())))
