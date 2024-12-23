def high_order_function(func, name):
    func(name)

def say_hello(text):
    print(f"Hola {text}")

high_order_function(say_hello, "Profesor Búho")

def multiplicador(factor):
    def multiplica(numero):
        return numero * factor
    return multiplica

multiplica_por_3 = multiplicador(3)
resultado = multiplica_por_3(8)
print( resultado )


list_1 = [1, 2, 3, 4]
result_1 = list(map(lambda n: n**2, list_1))
print(result_1)

list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda n: n%2 == 0, list_2))
print(pares)

from functools import reduce

suma = reduce(lambda x, y: x + y, list_1)
print(suma)