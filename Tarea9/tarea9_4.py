#Definir lista vacia
lista=[]
#Agregamos 5 alturas
for x in range(5)
    valor=input("Introduce una altura:")
    lista.append(valor)
#Visualizar promedio
suma=0
for x in range(5):
    suma=suma+lista[x]
promedio=suma/5
print("La altura media es ",promedio)

#Visualizar cuantos superan la media y los que no
supera=0
nosupera=0
for x in range(5):
    if lista[x]>promedio:
        supera=supera+1
    else:
        nosupera=nosupera+1
print("Persona superior a la media:",supera)
print("Persona inferior a la media:",nosupera)
print()