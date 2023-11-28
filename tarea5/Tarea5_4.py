n=int(input("Triangulos?"))
for x in range(n):
    lado1=float(input("Lado1:"))
    lado2=float(input("Lado2:"))
    lado3=float(input("Lado3:"))
    if lado1==lado2 and lado1==lado3:
        print("Triangulo Equilatero")
        equilatero=equilatero+1
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("Triangulo Isosceles")
            isosceles=isosceles+1
        else:
            print("Triangulo Escaleno")
            escaleno=escaleno+1

print("Cantidad de Equilatero:",Equilatero)
print("Cantidad de Isosceles:",Isosceles)
print("Cantidad de Escaleno:",Escaleno)
