def suma_pares_hasta_num(numero):
    suma = 0
    for i in range(2, numero + 1, 2):
        suma += i
    return suma
try:
    numero = int(input("Ingrese un número: "))
    
    if numero < 1:
        print("Ingrese un número mayor o igual a 1.")
    else:
        resultado = suma_pares_hasta_num(numero)
        print(f"La suma de todos los números pares desde 1 hasta {numero} es: {resultado}")

except ValueError:
    print("Por favor, ingrese un número entero válido.")
