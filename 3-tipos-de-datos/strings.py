# string_1 = "Profesor Búho"
# string_2 = 'Hola mundo'

# print(string_1)
# print( type(string_1) )
# print(string_2)
# print( type(string_2) )

# string_3 = 'I\'m Profesor Búho'

# print(string_3)
# print( type(string_3) )

# string_4 = '25.4'
# number_1 = 25.4

# print(string_4)
# print( type(string_4) )
# print(number_1)
# print( type(number_1) )

# string_5 = string_3 + ' ' + string_4
# print(string_5)

# string_6 = str(number_1)
# print(string_6)
# print( type(string_6) )

# number_2 = float(string_4)
# print(number_2)
# print( type(number_2) )

# print( string_1[-4] )
# print( string_1[0:10:2] )
# print( string_1[9:] )
# print( string_1[:8] )
# print( string_1[0::2] )

# string_ejercicio = 'Mi nombre es Profesor Búho'
# print(string_ejercicio[13:])
# print(string_ejercicio[0:9])
# print(string_ejercicio[3:9])
# print(string_ejercicio[-13])
# print(string_ejercicio[0::3])

# Métodos para Strings
string_7 = "hola mundo"
string_8 = "HOLA MUNDO"
string_9 = "           HOLA MUNDO         "
string_10 = "Profesor Búho"
string_11 = "12456clave"
string_12 = "12456"

print( string_7.capitalize() )
print( string_7 )
print( string_7.upper() )
print( string_8.lower() )
print( string_7.title() )
print( string_7.split() )
print( string_9 )
print( string_9.strip() )
print( string_9.lstrip() )
print( string_9.rstrip() )
print( string_7.replace('o', '0') )
print( "Profesor Búho".replace('Búho', '') )

print( len(string_7) )
print( string_7.count('o') )
print( string_10.find('o') )
print( string_10.rfind('o') )
print( string_10.find('ñ') )
print( string_10.find('r', 3, 8) )
print( string_10.index('s') )
print( string_10.rindex('ú') )
print( string_10.startswith('P') )
print( string_10.endswith('úho') )
print( string_11.isalnum() )
print( string_11.isalpha() )
print( string_12.isdigit() )
print( string_8.isupper() )
print( string_7.islower() )