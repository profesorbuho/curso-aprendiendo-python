# # Creando o definiendo una función
# def sumar(a, b):
#     print( f"La suma de a y b es: {a + b}" )
#     return a + b

# # Llamando a la función
# sumar(5, 9)
# suma_ab = sumar(15, 65)
# print( suma_ab )

# print(suma_ab + 20)

def is_int(number_string):
    if number_string.isdigit():
        return int(number_string)
    else:
        print("El valor ingresado es incorrecto.")
        exit()

numero = input( "Ingrese un número entero: " )
numero_entero = is_int(numero)
print( f"El número ingresado es un valor entero: {numero_entero}" )
print( type(numero_entero) )