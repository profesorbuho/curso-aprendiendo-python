def factorial(n):
    if n == 0:  # Caso base
        return 1
    else:
        return n * factorial(n-1) # Llamado a la función
    
factorial_5 = factorial(5)
print( factorial_5 )