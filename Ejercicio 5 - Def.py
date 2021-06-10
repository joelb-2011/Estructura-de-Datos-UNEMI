"""Funciones sin retorno"""
def vocales(frase):
     for car in frase:
         if car in('a','e','i','o','u'):
            print(car)
"""Llamada a funcion"""
oracion = input('Ingrese una oracion: ')
vocales(oracion.lower())
"""Funcion con retorno de valor"""
def promedio(nota):
    summ = 0
    for n in nota:
        summ += n
    return summ / len(nota)
# llamada a funcion
listanota = [8, 2, 12, 14, 14]
prom = promedio(listanota)
print('Promedio: {} = {}'.format(listanota, prom))
