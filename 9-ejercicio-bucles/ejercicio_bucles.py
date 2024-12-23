# Crear una lista
list_1 = []
length = input( "Ingrese la cantidad de números que va a contener su lista: " )
if length.isdigit():
    length = int(length)
else:
    print( "El valor ingresado es incorrecto, se permite unicamente números enteros positivos." )
    exit()

while len(list_1) < length:
    element = input( "Ingresa un número entero como elemento de la lista: " )
    if element.isdigit():
        list_1.append(int(element))
    else:
        print( "El valor ingresado es incorrecto, intentalo nuevamente." )

print( list_1 )

# Ordenar lista
copy_list = list(list_1)
c = -1

for i in list_1:
    copy_list.remove(i)
    if i > copy_list[c]:
        copy_list.append(i)
        c = -1
    else:
        c -= 1
        while c != -1:
            if c == -len(list_1):
                copy_list.insert(0, i)
                c = -1
            elif i > copy_list[c]:
                copy_list.insert(c+1, i)
                c = -1
            else:
                c -= 1

print(f"La lista ordenada es: {copy_list}")