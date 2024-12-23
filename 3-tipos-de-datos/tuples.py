tuple_1 = ( 2, "hola", 5.48, ["a", "b", "c"], (8, 7, 5) )
print( tuple_1 )
print( type(tuple_1) )

print( tuple_1[3] )
print( tuple_1[4] )
print( tuple_1[2:4] )

list_1 = list(tuple_1)
print(list_1)

list_1.append(63)
print(list_1)

tuple_1 = tuple(list_1)
print( tuple_1 )

# Desempaquetar un tupla
tuple_2 = (2, 4, 6)
number_2, number_4, number_6 = tuple_2
print( number_2 )
print( number_4 )
print( number_6 )

# Concatenar tuplas
tuple_3 = tuple_1 + tuple_2
print( tuple_3 )

# Multiplicar tuplas
tuple_4 = tuple_2 * 4
print( tuple_4 )

# Métodos para tuplas
print( tuple_3.count(2) )
index_list = tuple_3.index(['a', 'b', 'c'])
print(index_list)

print( "En la tupla 2, el índice 2 contiene el valor", tuple_2[2] )

# Ejercicio de práctica
tuple_5 = ("Profesor Búho", 28, 171)
tuple_6 = ("Ecuador", [2023, 2024, 2025])

print(tuple_5, tuple_6)

user_info = tuple_5 + tuple_6
print( user_info )

print( "Mi nombre es", user_info[0], "tengo", user_info[1], "años, mi estatura es", user_info[2], "centimetros, vivo en", user_info[3], "y el año actual es", user_info[4][1])

year_5 = user_info[4][1] + 5
age_5 = user_info[1] + 5

print( "Dentro de 5 años, en el año", year_5, "voy a tener", age_5, "años." )