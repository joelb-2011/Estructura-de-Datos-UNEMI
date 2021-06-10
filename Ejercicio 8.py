"""num = 10
num = '20'
if type(num)==int:
    num=num*2
else:
    print("El valor no es numerico.")
    
def mensaje(msg):
    print(msg)

mensaje("Bienvenido a Python.")
mensaje("Mi primer programa.")"""

class Sintaxis:
    
    def __init__(self,dato="Instancia de la clase"):
        self.frase=dato
    
    def usoVariables(self):
        edad, _peso = 19, 68.6
        nombre = "Joel Barrionuevo"
        #          012345678910
        sexo = "M"
        estadocivil = True
        #print("civil={} y su tipo es: {}.".format(civil,type(civil)))

        usuario=()
        usuario = ('JoelB','2011','jbarrionuevos@unemi.edu.ec',True)
        
        #usuario[4]="milagro"
        x = usuario[0]
        materia = ['Estructura datos','PHP','POO']
        
        materia[1] = "Python"
        materia.append("SO")
        estudiante={}
        estudiante = {'nombre': 'Joel', 'edad':19, 'fac': 'faci'}
        estudiante["edad"]=20
        estudiante["cargo"]="Estudiante"
        y=estudiante["cargo"]
        #print(nombre,nombre[0],nombre[0:2],nombre[-1])
        #print(usuario,usuario[0],usuario[0:2],usuario[-1])
        #print(materia,materia[2:],materia[:2],materia[:-1],materia[-2:])
        print(x,y)
        print(estudiante,estudiante['nombre'])

    def mostrar(self):
        print("mostrar")
        print(self.frase)

ejer1 = Sintaxis()
ejer1.usoVariables()
#print(ejer1.frase)
#ejer1.mostrar()
