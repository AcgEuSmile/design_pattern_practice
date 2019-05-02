class PizzaStore(object):
    
    def orderPizza(self, type: str) -> object:
       pizza = self.createPizza(type) 
       pizza.prepare()
       pizza.bake()
       pizza.cut()
       pizza.box()

       return pizza
    
    def createPizza(self, type: str):
        raise("must be implementataion")

class NYStylePizzaStore(PizzaStore):

    def __init__(self):
        super(NYStylePizzaStore, self).__init__()
        self.ingredientFactory = NYPizzaIngredientFactory()
    def createPizza(self, type: str):
        
        if (type == "cheese"):
            return CheesePizza(self.ingredientFactory, name=type)
        elif (type == "veggie"):
            return VeggiePizza(self.ingredientFactory, name=type)
        else:
            return NULL

class ChicagoStylePizzaStore(PizzaStore):

    def __init__(self):
        super(ChicagoStylePizzaStore, self).__init__()
        self.ingredientFactory = ChicagoPizzaIngredientFactory()

    def createPizza(self, type: str):
        
        if (type == "cheese"):
            return CheesePizza(self.ingredientFactory, name=type)
        elif (type == "veggie"):
            return VeggiePizza(self.ingredientFactory, name=type)
        else:
            return NULL

class Pizza(object):
    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
    def prepare(self):
        # prepare method
        pass
    def bake(self):
        # bake method
        pass
    def cut(self):
        # cut method
        pass
    def box(self):
        # box method
        pass

class PizzaIngredientFactory(object):

    def createDough(self)->"Dough":
        pass
    def createSauce(self)->"Sauce":
        pass
    def creatCheese(self)->"Cheese":
        pass
    
class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super(NYPizzaIngredientFactory, self).__init__()
    def createDough(self)->"Dough":
        return ThinCrustDough() 
    def createSauce(self)->"Sauce":
        return MarinaraSause()
    def creatCheese(self)->"Cheese":
        return ReggianoCheese()
    
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super(ChicagoPizzaIngredientFactory, self).__init__()
    def createDough(self)->"Dough":
        return ThinCrustDough_ChicagoStyle() 
    def createSauce(self)->"Sauce":
        return MarinaraSause_ChicagoStyle()
    def creatCheese(self)->"Cheese":
        return ReggianoCheese_ChicagoStyle()

class CheesePizza(Pizza):
    def __init__(self, ingredientFactory, *args, **kwargs: 'name'):
        super(CheesePizza, self).__init__(*args, **kwargs)
        self.ingredientFactory = ingredientFactory
    def prepare(self):
        # prepare method
        dough = self.ingredientFactory.createDough()
        sauce = self.ingredientFactory.createSauce()
        cheese = self.ingredientFactory.creatCheese()
    def bake(self):
        # bake method
        pass
    def cut(self):
        # cut method
        pass
    def box(self):
        # box method
        pass

class Dough(object):
    def __init__(self):
        pass

class Sause(object):
    def __init__(self):
        pass

class Cheese(object):
    def __init__(self):
        pass

class ThinCrustDough(Dough):
    def __init__(self):
        super(ThinCrustDough, self).__init__()
        print("using ThinCrustDought")

class MarinaraSause(Sause):
    def __init__(self):
        super(MarinaraSause, self).__init__()
        print("using MarinaraSause")

class ReggianoCheese(Cheese):
    def __init__(self):
        super(ReggianoCheese, self).__init__()
        print("using ReggianoCheese")

class ThinCrustDough_ChicagoStyle(Dough):
    def __init__(self):
        super(ThinCrustDough_ChicagoStyle, self).__init__()
        print("using ThinCrustDought_ChicagoStyle")

class MarinaraSause_ChicagoStyle(Sause):
    def __init__(self):
        super(MarinaraSause_ChicagoStyle, self).__init__()
        print("using MarinaraSause_ChicagoStyle")

class ReggianoCheese_ChicagoStyle(Cheese):
    def __init__(self):
        super(ReggianoCheese_ChicagoStyle, self).__init__()
        print("using ReggianoCheese_ChicagoStyle")
if __name__ == "__main__":
    pizza_store = NYStylePizzaStore()
    pizza_store.orderPizza("cheese")
    pizza_store2 = ChicagoStylePizzaStore()
    pizza_store2.orderPizza("cheese")