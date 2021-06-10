"""Uso de While infinito"""
c = 1
while True:
    print(c)
    break
    
# while validacion
vocal = input("Ingrese una vocal: ")
while vocal not in("a","e","i","o","u"):
    if vocal == ".":
        break
    vocal = input("Vocal: ")
print("Su vocal o punto es:{}".format(vocal))
