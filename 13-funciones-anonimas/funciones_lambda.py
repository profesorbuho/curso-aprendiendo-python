producto = lambda a, b: a * b
producto_5_9 = producto(5, 9)
print(producto_5_9) 
print( producto(6, 8) )

def product(c, d):
    return c * d

product(7, 7)

# Posicion final
x_f = lambda x_o, v_o, t, a: x_o + v_o*t + (1/2)*a*(t**2)
posicion = x_f(30, 5, 12, 1)
print(posicion)