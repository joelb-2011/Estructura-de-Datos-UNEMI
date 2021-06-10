# Tuplas – Listas - Diccionarios
usuario = ("JoelB","2011","jbarrionuevos@unemi.edu.ec")
materia = ["Python","PHP","POO","SO"]
estudiante = {"nombre":"Joel Barrionuevo","edad":19,"fac":"faci"}
print(usuario[0],materia[1],estudiante['nombre'])
print(usuario[0:2],estudiante.keys(),estudiante.values())
materia.append("Estructura datos")
estudiante["sexo"], estudiante["edad"]="M", 19
print(materia,estudiante)
#tupla,lista,diccionario=(),[],{}
# Recorridos tuplas y listas con in
for valor in usuario: print(valor)
# Recorridos listas con enumerate
for i, c in enumerate(materia): print(i,':',c)
# Recorridos diccionario con items
for c, v in estudiante.items(): print(c,':',v)
