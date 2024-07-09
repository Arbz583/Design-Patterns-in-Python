from abc import ABC, abstractmethod
from caramel import Caramel

class Image:
    pass

class Filter(ABC):

    @abstractmethod
    def apply(self, image:Image):
        pass

class VividFilter(Filter):

    def apply(self, image: Image):
        print("Applying Vivid Filter")

class ImageView:

    def __init__(self, image:Image) -> None:
        self.image = image

    def apply(self, filter:Filter):
        filter.apply(self.image)

# using composition
class CaramelFilter(Filter):

    def __init__(self, caramel:Caramel):
        self.caramel = caramel

    def apply(self, image: Image):
        self.caramel.init()
        self.caramel.render(image)

# using inheritence
class CaramelAdapter(Filter, Caramel):

    def apply(self, image: Image):
        self.init()
        self.render(image)

image_view = ImageView(Image())
image_view.apply(VividFilter())
image_view.apply(CaramelFilter(Caramel()))
image_view.apply(CaramelAdapter())