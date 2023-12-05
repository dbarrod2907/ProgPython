def calcular(n):
    meses=["No existe","Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    if n<1 or n>12:
        print(meses[0])
    else:
        print(meses[n])


a=int(input("Ingresa un numero: "))
calcular(a)
