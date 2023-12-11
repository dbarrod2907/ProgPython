"""El ordenador piensa un número y debes acertarlo en menos de 10 intentos
"""

from random import randint
aleatorio=randint(1,100)
#Variable de control para salir del bucle
control=0
#Almacenamos el numero de intentos
intentos=0
while intentos<10 and control==0:
    numero=int(input("Numero:"))
    intentos=intentos+1
    if numero<aleatorio:
        print("Debes introducir un numero mayor")
    else:
        print("Acertaste en ",intentos," intentos")
        control=1
if control==0:
    print("¡Esto no es lo tuyo!")


