from abc import ABC, abstractmethod
from token import ENCODING

class ViewEngine(ABC):

    @abstractmethod
    def render(self, view_name:str, context:dict) -> str:
        pass

class MatchaViewEngine(ViewEngine):

    def render(self, view_name:str, context:dict):
        return "view rendered by Matcha"

class Controller:
    
    def render(self, view_name:str, context:dict):
        engine:ViewEngine = self._create_view_engine()
        html = engine.render(view_name, context)
        print(html)
    
    def _create_view_engine(self) ->ViewEngine:
        return MatchaViewEngine()