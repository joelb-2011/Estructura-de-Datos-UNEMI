class For:

    def __init__(self,lim=6):
        self.n=lim

    def usoFor(self):
        nombre = "Joel"
        datos = ["Joel",19,True]
        numeros = (2,5.6,4,1)
        estudiante = {'nombre': 'Joel', 'edad': 19, 'fac': 'faci'}
        listaNotas = [(30,40),(20,40,50),(50,40)]
        listaAlumnos = [{"nombre": "Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #for i in range(5):
        #    print("i={}".format(i))
        #for i in range(2,5):
        #    print("i={}".format(i))
        #for i in range(10,2,-2):
        #    print("i={}".format(i))
        #for i in range(3,self.n,3):
        #    print("i={}".format(i),end=" ")
        
        #long = len(nombre)
        #for pos in range(long):
        #    print(nombre[pos],end= " ")
            
        #long = len(datos)
        #for pos in range(long):
        #    print(datos[pos],end= " ")
        #for pos,elem in enumerate(nombre):
        #    print(pos," ",elem)
        
        #for elem in datos:
        #    print(elem)
        #for num in numeros:
        #    print(num)
        
        #for pos,elem in enumerate(nombre):
        #    if pos%2==0 and pos!=0:
        #        print(elem)
        #estudiante = {'nombre': 'Joel', 'edad': 19, 'fac': 'faci'}
        #for clave,valor in docente.items():
        #    print(clave,valor,end=" ")
        #lista = [2,4,5,5]
        #acu=0
        #for ele in lista:
        #    acum=acum+ele
        #print(acu)
        #acu=0
        #listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #for alumnos in listaAlumnos:
        #    print(alumnos)
        #    acu = acu + alumnos["final"]
        #print(acu)
        #acu=0
        #listaAlumnos = [{"nombre":"Erick","final":70},{"nombre":"Yady","final":60},{"nombre":"Danny","final":90}]
        #for alumnos in listaAlumnos:
        #    for c,v in alumnos.items():
        #        print(c,v)
        #        if c=="final":
        #            acu=acu+v
        #print(acu,acu/len(listaAlumnos))
        listaNotas = [(30,40),(20,40,50),(50,40,10,45),(5,15)]
        acu,cont=0,0
        for notas in listaNotas:
            print(notas)
            acumParcial=0
            for nota in notas:
                acumParcial+=nota
            cont+= len(notas)
            acu+= acumParcial
            print(acumParcial,acumParcial/len(notas))
        print(acu,acu/cont)
                

bucle1 = For()
bucle1.usoFor()

#bucle2 = For(12)
#bucle2.usoFor()
#print(bucle.numero)
