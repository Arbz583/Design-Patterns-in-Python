from abc import ABC, abstractmethod

class Compressor(ABC):

    @abstractmethod
    def compress(self):
        pass

class Filter(ABC):

    @abstractmethod
    def apply(self):
        pass

class GpegCompressor(Compressor):

    def compress(self):
        print("compressing")

class BlacAndWhiteFilter(Filter):

    def apply(self):
        print("applying filter")

class ImageStorage():

    def store(self, compressor:Compressor, filter:Filter):
        compressor.compress()
        filter.apply()

image_storage = ImageStorage()
image_storage.store(GpegCompressor(), BlacAndWhiteFilter())