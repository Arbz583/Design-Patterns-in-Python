from itertools import product
from factory import (
    Controller, 
    MatchaViewEngine,
    ViewEngine,
)

class SharpViewEngine(ViewEngine):

    def render(self, view_name:str, context:dict):
        return "view rendered by Sharp"

# Controller with Sharp engine
class SharpController(Controller):

    def _create_view_engine(self):
        return SharpViewEngine()


class ProductsController(SharpController):

    def product_list(self):

        # get products from a database
        # context["product"] = product obj
        context = dict()  
        self.render('products/list.html', context)

product_controller = ProductsController()
product_controller.product_list()
        
    

