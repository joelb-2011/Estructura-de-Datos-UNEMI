class Buscador:
    def __init__(self,lista):
        self.lista=datos

    def recorrerElemento(self):
        for ele in self.lista:
            print(ele,end=" ")

        for ele in self.lista[::-1]:
            print(ele,end=" ")

        print()
        for pos,ele in enumerate(self.lista):
            print("[{}]={} ".format(pos,ele))
        print()

        for pos in range(len(self.lista)-1,-1,-1):
            print("[{}]={} ".format(pos,self.lista[pos]))

    def buscar(self,buscado):
        encontrado=False
        for pos,ele in enumerate(self.lista):
            if ele==buscado:
                encontrado=True
                break

        if encontrado:
            return pos
        else:
            return -1


datos = [2,3,1,5,8]
bus = Buscador(datos)
#valor=9
#resp= bus.buscar(valor)
#if resp != 1:
#    print("el numero:{} se encuentra en la posicion:[{}] de la lista:{}".format(valor,resp,bus.lista))
#else:
#    print("el numero:{} no se encuentra en la lista:{}".format(valor,bus.lista))
numerosBuscados = (2,4,6,1)
respuestas = {}
for valor in numerosBuscados:
    resp= bus.buscar(valor)
    if resp !=-1:
        respuestas[valor]=resp
print(respuestas)
