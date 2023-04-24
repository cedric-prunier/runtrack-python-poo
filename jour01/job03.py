class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        print(self.nombre1 + self.nombre2)


op1 = Operation(12, 3)
op1.addition()
