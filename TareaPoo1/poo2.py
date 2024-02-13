class Triangulo:
    def __init__(self,l1,l2,l3):
        self.lado1=l1
        self.lado2=l2
        self.lado3=l3

    def imprimirMayor(self):
        print("Medida del lado Mayor:")
        if self.lado1>self.lado2 and self.lado1>self.lado3
            print(self.lado1)
        else:
            if self.lado2>self.lado3
                print(self.lado2)
            else:
                print(self.lado3)
    def equilatero(self):
        if (self.lado1==self.lado2 and self.lado1==self.lado3):
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")

#Principal
l1=int(input("Lado1:"))
l2=int(input("Lado2:"))
l3=int(input("Lado3:"))
triangulo1=Triangulo(l1,l2,l3)
triangulo1.imprimirMayor()
triangulo1.equilatero()
