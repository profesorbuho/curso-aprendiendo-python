dic_1 = { 
    "nombre": "Profesor Búho",
    "edad": 28,
    "pais": "Ecuador",
    "lenguajes": ["Python", "Java", "JavaScript", "C++"],
    "estatura": 171,  # centímetros
 }

print( dic_1 )
print( type(dic_1) )

print( dic_1["lenguajes"][2] )

dic_1["edad"] = 32
print( dic_1 )

# Operaciones
print( "estatura" in dic_1 )

print( len(dic_1) )

list_1 = list(dic_1)
print( list_1 )

# Métodos para diccionarios
print( dic_1.get("estatura") )
print( dic_1.keys() )
print( dic_1.values() )
print( dic_1.items() )
value = dic_1.pop("pais")
print( dic_1 )
print( value )
