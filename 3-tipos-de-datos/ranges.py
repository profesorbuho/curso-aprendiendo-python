range_1 = range(0, 10, 2)
list_1 = list( range_1 )

print( list_1 )
print(range_1)
print( type(range_1))

# Indexables
print( range_1[2] )

# Operador in
print( 6 in range_1 )

#Funciones
print( len(range_1) )
print( min(range_1) )
print( max(range_1) )

#Métodos
print( range_1.count(6) )
print( range_1.index(8) )