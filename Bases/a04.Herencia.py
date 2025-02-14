
class Padre:
    def __init__(self):
        print("Soy padre")

    def saludar(self):
        print("Hola dentro de padre")
        
class Madre:
    def __init__(self):
        print("Soy madre")

    def comer(self):
        print("Dentro de comer")

class Hijo(Madre, Padre):
    def __init__(self):
        # super().__init__()
        Padre.__init__(self)
        Madre.__init__(self)
        print("Soy hijo")
    
    def saludar(self):
        super().saludar()
        print("Dentro de hijo")
        
# padre = Padre()
# padre.saludar()

hijo = Hijo()
hijo.saludar()
hijo.comer()