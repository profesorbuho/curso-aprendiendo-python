import fibonacci as fib
from operaciones import suma, resta, producto, division
import math
import pyfiglet

fibonacci_10 = fib.fibonacci(10)
print( fibonacci_10 )

number_pi = fib.PI
print( number_pi )

result_1 = suma(5, 8)
print(result_1)

result_2 = resta(26, 5)
print( result_2 )

result_3 = producto(2, 7)
print( result_3 )

result_4 = division(49, 7)
print( result_4 )

result_5 = math.sqrt(64)
print( result_5 )

def text_ascii(texto):
    return pyfiglet.figlet_format(texto)

result_6 = text_ascii("Profesor Buho")
print( result_6 )