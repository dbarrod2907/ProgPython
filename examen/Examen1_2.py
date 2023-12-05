def contar_cifras_de_un_num(numero):
    numero = abs(numero)
      
    longitud = len(str(numero))
    return longitud
try:
    numero = int(input("Ingrese un número: "))
    
    resultado = contar_cifras(numero)
    
    print(f"El número {numero} tiene {resultado} cifras.")

except ValueError:
    print("Por favor, ingrese un número entero válido.")
