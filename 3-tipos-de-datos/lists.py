list_1 = [ "Hola", "Profesor", "Búho" ]
list_2 = [ 5, 6.48, "a", "c", [1, 2, 3] ]

print(list_1)
print( type(list_1) )
print(list_2)
print( type(list_2) )

print( list_2[3] )
print( list_2[4] )
print( list_2[4][1] )

print( list_1[1][3] )

print(list_1)
list_1[0] = "Hello"
print(list_1)
list_1.append("Qué tal")
print(list_1)

list_3 = list_2
print(list_3)
list_2[1] = 6.24
print(list_2)
print(list_3)

print( id(list_2) )
print( id(list_3) )

list_3 = list( list_2 )
print( id(list_2) )
print( id(list_3) )
list_2[1] = 4.12
print(list_2)
print(list_3)

# Concatenar listas
list_4 = list_1 + list_2
print( list_4 )

# Multiplicar listas
list_5 = list_1 * 2
print(list_5)

# Funciones para listas
print( len(list_2) )
print(list_2)

list_6 = [ 2, 7, 95, 46, 121.5, 8 ]
list_10 = list_6.copy()
print( min(list_6) )
print( max(list_6) )

list_7 = [ "Hola", "Cómo", "estas" ]
print( min(list_7) )
print( max(list_7) )

list_8 = [ "v", "Z", "e", "p", "o", "p" ]
list_11 = list_8.copy()
print( min(list_8) )
print( max(list_8) )

# Métodos para listas
index_e = list_8.index("e")
print( index_e )

counter = list_8.count("p")
print( counter )

print(list_6)
list_6.clear()
print(list_6)

list_9 = list_7.copy()
print(list_9)

print(list_7)
list_7.append("Búho")
print(list_7)

print(list_8)
list_8.extend([2, 4, 6, "e", "x"])
print(list_8)

list_8.insert(4, "f")
print(list_8)

list_8.pop()
print(list_8)
list_8.pop(6)
print(list_8)

list_8.remove("e")
print(list_8)

list_8.reverse()
print(list_8)

print(list_10)
list_10.sort()
print(list_10)
list_10.sort(reverse=True)
print(list_10)

print(list_11)
list_11.sort()
print(list_11)
list_11.reverse()
print(list_11)