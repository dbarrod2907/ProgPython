#funcion creamos una lista de n empleados
def crearLista(n):
    articulos=[]
    precios=[]
    for x in range(n):
        articulo=input("Introduce el nombre del articulo:")
        precio=int(input("Introduce el precio del articulo:"))
        articulos.append(articulo)
        precios.append(precio)
    return [articulos,precios]

#funcion visualizar los articulos y sus precios
def verArticulos(articulos,precios):
    for x in range(len(articulos)):
        print(articulos[x],":",precios[x])
        
#funcion articulo mas caro
def articuloMasCaro(articulos,precios):
    masCaro=precios[0]
    pos=0
    for x in range(1,len(precios)):
        if precios[x]>masCaro:
            masCaro=precios[x]
            pos=x
    print("El articulo mas caro es ",articulos[pos]," con un precio de ",masCaro)

#funcion articulo con precio menor a uno dado
def articulosMenores(articulos,precios,importe):
    for x in range(len(precios)):
        if precios[x]<importe:
            print(articulos[x]," tiene un precio menor a ",importe," y es ",precios[x])
#Programa principal

n=int(input("¿Cuantos articulos hay? "))
articulos,precios=crearLista(n)
verArticulos(articulos,precios)
articuloMasCaro(articulos,precios)
importe=int(input("Importe a comparar:"))
articulosMenores(articulos,precios,importe)

