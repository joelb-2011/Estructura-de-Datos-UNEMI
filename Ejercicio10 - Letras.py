class Ciclo:

    def __init__(self,num=10):
        self.numero=num

    def usoWhile(self):
        print("Dentro de la clase.",self.numero)

        caracter=""
        while caracter not in('a','e','i','o','u'):
            caracter = input("Ingrese una vocal: ")
            #caracter = caracter.lower()

        print("Felicitaciones, el caracter ingresado: {} es una vocal.".format(caracter))

ciclo1 = Ciclo()
#print("Fuera de la clase",ciclo1.numero)
print(ciclo1.usoWhile())
