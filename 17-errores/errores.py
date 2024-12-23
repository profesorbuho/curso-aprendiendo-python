def sumar(a, b):
    return a + b

resultado = sumar(5, 9)
print( resultado )

print( "Hola mundo" )

# division = 8 / 0
# print( division )

# resultado_1 = division(25, 0)
# print( resultado_1 )

# print( resta )
# print( "hola" + 75 )

# lista = [1, 2, 3, 4]
# print( lista[10] )

def division_de_enteros(c, d):
    try:
        result = c / d
        if c%1 !=0 or d%1 !=0:
            raise ValueError( f"Los números {c} y {d} deben ser valores enteros." )
    except ZeroDivisionError:
        print( f"El argumento d = {d} debe ser diferente de cero." )
    except TypeError:
        print( f"Los argumentos {c} y {d} deben ser valores numéricos." )
    else:
        return result
    finally:
        print( "La función terminó de ejecutarse." )
    
# resultado_2 = division_de_eneteros(4, "0")
resultado_3 = division_de_enteros(4, 2)
print( resultado_3 )
