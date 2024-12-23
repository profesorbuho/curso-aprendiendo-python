# condition = True
# counter = 0

# while condition:
#     print( counter )
#     counter += 1

#     if counter >= 6:
#         condition = False

# print( "El bucle while ha terminado" )

# list_1 = ["Hola", "mundo", "Profesor", "Búho"]
# index = 0

# while index < 4:
#     print( list_1[index] )
#     index += 1

# print("El bucle ha finalizado")

password = "ProfesorBuho123"
condition = True
counter = 0
tries = 3

print("Ingresa tu contraseña solo tienes 3 oportunidades.")

while condition:
    password_input = input( "Ingresa tu contraseña: " )
    if password == password_input:
        print("La contraseña ingresada es correcta.")
        break
    else:
        tries -= 1
        print(f"Tu contraseña es incorrecta te quedan {tries} intentos.")
        counter += 1

    if counter == 3:
        print("Se terminaron los intentos, tu cuenta ha sido bloqueada.")
        condition = False

print( "El programa ha finalizado." )