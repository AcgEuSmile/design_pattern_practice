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

    def createPizza(self, type: str):
        
        if (type == "cheese"):
            return NYStyleCheesePizza(name=type)
        elif (type == "veggie"):
            return NYStyleVeggiePizza(name=type)
        else:
            return NULL

class ChicagoStylePizzaStore(PizzaStore):

    def __init__(self):
        super(ChicagoStylePizzaStore, self).__init__()

    def createPizza(self, type: str):
        
        if (type == "cheese"):
            return ChicagoStyleCheesePizza(name=type)
        elif (type == "veggie"):
            return ChicagoStyleVeggiePizza(name=type)
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

class NYStyleCheesePizza(Pizza):
    def __init__(self, *args, **kwargs):
        super(NYStyleCheesePizza, self).__init__(*args, **kwargs)
    def prepare(self):
        # prepare method
        print("prepare NY cheese pizza")
        print("using ThinCrustDought")
        print("using MarinaraSause")
        print("using ReggianoCheese")
    def bake(self):
        # bake method
        print("bake NY cheese pizza")
    def cut(self):
        # cut method
        print("cut NY cheese pizza")
    def box(self):
        # box method
        print("box NY cheese pizza")

class NYStyleVeggiePizza(Pizza):
    def __init__(self, *args, **kwargs):
        super(NYStyleVeggiePizza, self).__init__(*args, **kwargs)
    def prepare(self):
        # prepare method
        print("prepare NY veggie pizza")
        print("using ThinCrustDought")
        print("using MarinaraSause")
    def bake(self):
        # bake method
        print("bake NY veggie pizza")
    def cut(self):
        # cut method
        print("cut NY cheese pizza")
    def box(self):
        # box method
        print("box NY cheese pizza")

class ChicagoStyleCheesePizza(Pizza):
    def __init__(self, *args, **kwargs):
        super(ChicagoStyleCheesePizza, self).__init__(*args, **kwargs)
    def prepare(self):
        # prepare method
        print("prepare Chicago cheese pizza")
        print("using ThinCrustDought_ChicagoStyle")
        print("using MarinaraSause_ChicagoStyle")
        print("using ReggianoCheese_ChicagoStyle")
    def bake(self):
        # bake method
        print("bake Chicago cheese pizza")
    def cut(self):
        # cut method
        print("cut Chicago cheese pizza")
    def box(self):
        # box method
        print("box Chicago cheese pizza")

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(self, *args, **kwargs):
        super(ChicagoStyleVeggiePizza, self).__init__(*args, **kwargs)
    def prepare(self):
        # prepare method
        print("prepare Chicago veggie pizza")
        print("using ThinCrustDought_ChicagoStyle")
        print("using MarinaraSause_ChicagoStyle")
    def bake(self):
        # bake method
        print("bake Chicago veggie pizza")
    def cut(self):
        # cut method
        print("cut Chicago cheese pizza")
    def box(self):
        # box method
        print("box Chicago cheese pizza")

if __name__ == "__main__":
    pizza_store = ChicagoStylePizzaStore()
    pizza_store.orderPizza("cheese")
    pizza_store.orderPizza("veggie")
    pizza_store2 = NYStylePizzaStore()
    pizza_store2.orderPizza("cheese")
    pizza_store2.orderPizza("veggie")