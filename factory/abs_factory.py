
class Pizza(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.dough = kwargs['dough']
        self.sauce = kwargs['sauce']

    def prepare(self):
        # prepare method
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method

class PizzaIngredientFactory(object):

    def createDough(self)->Dough:
        pass
    def createSauce(self)->Sauce:
        pass
    def creatCheese(self)->Cheese:
        pass
    
class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super(NYPizzaIngredientFactory, self).__init__()
    def createDough(self)->Dough:
        return ThinCrustDough() 
    def createSauce(self)->Sauce:
        return MarinaraSause()
    def creatCheese(self)->Cheese:
        return ReggianoCheese()
    
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super(ChicagoPizzaIngredientFactory, self).__init__()
    def createDough(self)->Dough:
        return ThinCrustDough_ChicagoStyle() 
    def createSauce(self)->Sauce:
        return MarinaraSause_ChicagoStyle()
    def creatCheese(self)->Cheese:
        return ReggianoCheese_ChicagoStyle()

class NYStyleCheesePizza(Pizza):
    def __init__(delf, *args, **kwargs):
        super(NYStyleCheesePizza, self).__init__(args, kwargs)
        self.ingredientFactory = NYPizzaIngredientFactory()
    def prepare(self):
        # prepare method
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.creatCheese()
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method

class CHicagoStyleCheesePizza(Pizza):
    def __init__(delf, *args, **kwargs):
        super(CHicagoStyleCheesePizza, self).__init__(args, kwargs)
        self.ingredientFactory = CHicagoPizzaIngredientFactory()
    def prepare(self):
        # prepare method
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.creatCheese()
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method