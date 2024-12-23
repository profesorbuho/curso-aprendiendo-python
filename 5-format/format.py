nombre = "Profesor Búho"
edad = 28
phrase_1 = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)

print( phrase_1 )

phrase_2 = "El {0} salta sobre el {1}.".format("gato", "perro")
print( phrase_2 )

phrase_3 = "Hola mi nombre es {nombre} y tengo {edad} años.".format(nombre="Ana", edad=30)
print( phrase_3 )

price = 49.8754
text = "El precio es {:.2f}".format(price)
print( text )

person = {
    "name": "Juan",
    "age": 40
}
text_1 = "Hola mi nombre es {name} y tengo {age} años.".format(**person)
print( text_1 )

# nombre_mascota = input("Escribe el nombre de tu mascota: ")
# edad_mascota = int(input("Escribe la edad de tu mascota: "))

# print( type(nombre_mascota) )
# print( type(edad_mascota) )

# text_2 = f"Mi mascota se llama {nombre_mascota} y tiene {edad_mascota} años."
# print( text_2 )

list_1 = [1, 2, 3, 4]

text_3 = f"El elemento de la posición 3 de la lista es: {list_1[3]}"
print( text_3 )

text_4 = f"Hola su nombre es {person["name"]} y tiene {person["age"]} años."
print( text_4 )
