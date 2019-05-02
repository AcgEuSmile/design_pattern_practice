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
        
        if (type.equals("cheese")):
            return NYStyleCheesePizza()
        elif (type.equals("veggie")):
            return NYStyleVeggiePizza()
        else:
            return NULL

class ChicagoStylePizzaStore(PizzaStore):

    def __init__(self):
        super(ChicagoStylePizzaStore, self).__init__()

    def createPizza(self, type: str):
        
        if (type.equals("cheese")):
            return ChicagoStyleCheesePizza()
        elif (type.equals("veggie")):
            return ChicagoStyleVeggiePizza()
        else:
            return NULL

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


class NYStyleCheesePizza(Pizza):
    def __init__(delf, *args, **kwargs):
        super(NYStyleCheesePizza, self).__init__(args, kwargs)
    def prepare(self):
        # prepare method
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method

class NYStyleVeggiePizza(Pizza):
    def __init__(delf, *args, **kwargs):
        super(NYStyleVeggiePizza, self).__init__(args, kwargs)
    def prepare(self):
        # prepare method
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method

class ChicagoStyleCheesePizza(Pizza):
    def __init__(delf, *args, **kwargs):
        super(ChicagoStyleCheesePizza, self).__init__(args, kwargs)
    def prepare(self):
        # prepare method
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method

class ChicagoStyleVeggiePizza(Pizza):
    def __init__(delf, *args, **kwargs):
        super(ChicagoStyleVeggiePizza, self).__init__(args, kwargs)
    def prepare(self):
        # prepare method
    def bake(self):
        # bake method
    def cut(self):
        # cut method
    def box(self):
        # box method