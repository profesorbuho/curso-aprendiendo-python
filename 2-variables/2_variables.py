'''
El nombre de una variable debe comenzar con una letra o guion bajo. Después del primer carácter que debe cumplir estas características, puedes agregar cualquier otro carácter como números, letras, guiones bajos, etc.
'''

variable_1 = 'Profesor Buho'
_variable_2 = 'Hola mundo'
variable_3 = 'Hello world'

'''
Se recomienda usar snake_case para escribir los nombres, Python no permite espacios en el nombre de variables. Y aunque para nombrar archivos si lo permite, es mejor siempre usar esta convención.
'''

snake_case = 'sanek case'
variable_4 = 'texto'

'''
Es recomendable usar palabras en inglés, si nombramos en español debemos tener en cuenta el no usar tildes, la letra ñ, y otro tipo de caracteres únicos del alfabeto español.
'''

variable_5 = 'variable número 5'
name = 'Profesor Búho'
year = 2024

'''
Python es case sensitive, lo que quiere decir es que distingue entre mayúsculas y minúsculas, así si nombramos una variable con la misma palabra, pero usando distintas combinaciones entre mayúsculas y minúsculas, cada variable será diferente a las otras. Es recomendable siempre que se pueda nombrar las variables con letras minúsculas.
'''
edad = 25
Edad = 28

print(edad)
print(Edad)

'''
Nunca se debe nombrar una variable con el nombre de alguna función ya establecida en Python. Python tiene algunas funciones por defecto y si nosotros usamos el nombre de alguna de estas funciones como nombre de una variable, la función dejara de funcionar.
'''
print = 'Hola'
print(edad)