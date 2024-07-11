from enum import Enum, auto

class PointType(Enum):

    HOSPITAL = auto()
    CAFE = auto()
    RESTAURANT = auto()

class Point:

    def __init__(self, x, y, icon:"PointIcon") -> None:
        self.x = x
        self.y = y
        self.icon = icon
    
    def draw(self):
        print(f"{self.icon.type} at ({self.x }, {self.y})")

class PointIcon:
    def __init__(self, type:PointType, icon) -> None:
        self._type = type
        self.icon = icon

    @property
    def type(self):
        return self._type

class PointIconFactory:
    def __init__(self) -> None:
        # caching ...
        self.type_to_point_icon = dict()

    def get_point_icon(self, type:PointType):
        if not type in self.type_to_point_icon:
            # None: convert_to_bytes_array("hospital.jpg")
            point_icon = PointIcon(type, None)
            self.type_to_point_icon[type] = point_icon
            
        return self.type_to_point_icon[type]

class PointService:

    def __init__(self, icon_factory:PointIconFactory):
        self.icon_factory = icon_factory
        
    def get_points(self):
        points = []
        # pull request from db!
        cafe_point = Point(
            1,
            3, 
            self.icon_factory.get_point_icon(PointType.CAFE)
        )
        restaurant_point = Point(
            5,
            4, 
            self.icon_factory.get_point_icon(PointType.RESTAURANT)
        )
        
        points.extend([cafe_point, restaurant_point])


        return points
    
service = PointService(PointIconFactory())
for point in service.get_points():
    point.draw()

"""
Without implementing the Flyweight pattern, the following code:

p1 = PointIcon(...)
p2 = PointIcon(...)

will create two separate objects in memory.
Each call to PointIcon(...) creates a new instance of the PointIcon class,
so p1 and p2 will refer to different objects,
 even though they are initialized with the same value.
"""