#funcion que crea una lista de n caracteres
def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista?"))
    for x in range(n):
        valor=input("Introduce un elemento de la lista:")
        lista.append(valor)
    return lista

#funcion que devuelve la palabra con mas caracteres de una lista
def mascaracteres(lista):
    palabra=lista[0]
    for x in range(len(lista)):
        if len(lista[x])>len(palabra):
            palabra=lista[x]
    return palabra

#Programa principal
palabras=crearLista()
print(palabra)
print("Palabra con mas caracteres:",mascaracteres(palabras))
