from cargo import Cargo

class Empleado:
    secuencia=0
    
    def __init__(self,nom,car):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.cargo=car

    def generarCodigo(self):
        Empleado.secuencia=Empleado.secuencia+1
        return Empleado.secuencia
    def mostrar(self):
        print("({})-Nombre:{} ({})-Cargo:{} ".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descripcion))

cargo1 = Cargo("Estudiante")
emp1 = Empleado("Joel",cargo1)
emp1.mostrar()
