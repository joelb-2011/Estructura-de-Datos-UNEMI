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

    def ordenarAsc(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] > self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux
                        
    def ordenarDes(self):
        for pos in range(0,len(self.lista)-1):
            for sig in range(pos+1,len(self.lista)):
                if self.lista[pos] < self.lista[sig]:
                    aux = self.lista[pos]
                    self.lista[pos]=self.lista[sig]
                    self.lista[sig]=aux

    def primer(self):
        return self.lista[0]

    def primerElemento(self):
        primero=self.lista[0]
        self.lista = self.lista[1:]
        return primero

    def primerElemento2(self):
        primero=self.lista[0]
        auxlista=[]
        for pos in range(1,len(self.lista)):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return primero

    def ultimo(self):
        return self.lista[-1]

    def ultimoEliminado(self):
        ultimo=self.lista[-1]
        self.lista = self.lista[:-1]
        return ultimo

    def ultimoEliminado2(self):
        ultimo=self.lista[-1]
        auxlista=[]
        for pos in range(0,len(self.lista)-1):
            auxlista.append(self.lista[pos])
        self.lista=auxlista
        return ultimo

    def insertar(self,num):
        self.ordenarAsc()
        pass
        
datos = [10,15,18,20,30]
num=18
#datos.sort()
print(datos)
bus = Buscador(datos)
print(bus.ultimoEliminado2(),bus.lista)
#bus.ordenarAsc()
#print(bus.lista)
#bus.ordenarDes()
#print(bus.lista)

#valor=9
#resp= bus.buscar(valor)
#if resp != 1:
#    print("el numero:{} se encuentra en la posicion:[{}] de la lista:{}".format(valor,resp,bus.lista))
#else:
#    print("el numero:{} no se encuentra en la lista:{}".format(valor,bus.lista))
#numerosBuscados = (2,4,6,1)
#respuestas = {}
#for valor in numerosBuscados:
#    resp= bus.buscar(valor)
#    if resp !=-1:
#        respuestas[valor]=resp
#print(respuestas)
