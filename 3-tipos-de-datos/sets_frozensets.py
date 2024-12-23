set_1 = { 2, 7, 25, 40.2, 9, 7 }

print( set_1 )
print( type(set_1) )

frozenset_1 = frozenset( "abcdefgh" )
print( frozenset_1 )
print( type(frozenset_1) )

# Operaciones
print( 28 in set_1 )
print( "a" in frozenset_1 )
print( "c" not in frozenset_1 )

print( len(set_1) )
print( len(frozenset_1) )

# Métodos
set_1.add(95)
print( set_1 )
set_1.remove(40.2)
print( set_1 )
set_1.discard(7)
print( set_1 )
set_1.pop()
print( set_1 )
set_1.clear()
print( set_1 )

# Operaciones con conjuntos

set_2 = {5, 7, 95, 6, 4}
set_3 = {25, 7, 9, 6, 71}

# Union
union = set_2 | set_3
print( union )

# Intersección
intersection = set_2 & set_3
print( intersection )

# Diferencia
difference = set_2 - set_3
print( difference )

# Diferencia simétrica
simetric_difference = set_2 ^ set_3
print( simetric_difference )