class Condicion:

    def __init__(self,n1,n2):
        self.numero1=n1
        self.numero2=n2
        numero = self.numero1+self.numero2
        self.numero3=numero

    def Condicion(self):
        if self.numero1 == self.numero2:
            print("El Numero 1: {} y Numero 2: {} son iguales".format(self.numero1, self.numero2))
        elif self.numero1 < self.numero3:
            print("El Numero 1: {} es menor que Numero 3: {}".format(self.numero1, self.numero3))
        else:
            print("No son iguales.")
        print("Fin del metodo.")

condi1 = Condicion(5, 8)
print(condi1.numero3)
print(condi1.Condicion())
