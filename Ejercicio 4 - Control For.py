# for range(v) – range(vi,vf)  - range(vi,vf,inc)
frase = input("Ingrese una frase: ")
for ind in range(len(frase)):
    print(ind,'=',frase[ind])
# for in cadena - in(tupla) – in[lista]  
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
            print("Cantidad de vocales: {}".format(cvoc))
# Comprehension – [var for var in datos condicion]
[car for car in['a','e','i','o','u'] if car not in('a','i','o')]
