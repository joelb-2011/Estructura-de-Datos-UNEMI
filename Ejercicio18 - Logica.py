class Logica:
    def __init__(self):
        pass

    def par(self,numero):
        rec = numero % 2
        return rec

    def perfecto(self,numero):
        acu=0
        for divisor in range(1,numero):
            rec = numero%divisor
            if rec == 0:
                acu=acu+divisor
        return acu

    def divisoresNumero(self,numero):
        divisores = []
        for divisor in range(1,numero):
            rec = numero%divisor
            if rec == 0:
                divisores.append(divisor)
        return divisores

ejer = Logica()
numero = int(input("Ingrese Numero: "))
print(ejer.divisoresNumero(numero))
"""
numeros = (6,28,3,4)
for num in numeros:
    if ejer.perfecto(num) == num:
        print(num, "Perfecto")
"""
#num = numero = int(input("Ingrese un numero: "))
#numeros = [1,3,8,4,5,10]
#pares = []
#impares = {}
#for num in numeros:
#    if ejer.par(num) == 0:
#        pares.append(num)
#    else:
#        impares["Impares"]=num

#print(pares)
#print(impares)
