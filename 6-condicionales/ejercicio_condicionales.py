## Diccionario de datos del usuario
usuario = {}

## Obtener y verificar datos

# Nombre
nombre = input( "Ingresa tu nombre: " )
nombre = nombre.strip()
nombre_sin_espacios = nombre.replace(" ", "")
if nombre_sin_espacios.isalpha():
    usuario["nombre"] = nombre
else:
    print( "El nombre ingresado es incorrecto." )
    print( "Vuelve a ejecutar el programa." )
    exit()

# Edad
edad = input( "Ingresa tu edad: " )
if edad.isdigit():
    usuario["edad"] = int(edad)
else: 
    print( "La edad ingresada es incorrecta." )
    print( "Vuelve a ejecutar el programa." )
    exit()

# Ingresos
ingresos = input( "Ingresa tus ingresos anuales: " )
if ingresos.isdigit():
    usuario["ingresos"] = int(ingresos)
elif ingresos.find(".") != -1:
    ingresos_sin_punto = ingresos.replace(".", "", 1)
    if ingresos_sin_punto.isdigit():
        usuario["ingresos"] = round(float(ingresos), 2)
    else: 
        print( "El valor de ingresos es incorrecto." )
        print( "Vuelve a ejecutar el programa." )
        exit()
else:
    print( "El valor de ingresos es incorrecto." )
    print( "Vuelve a ejecutar el programa." )
    exit()

# Historial crediticio
historial_crediticio = input( "¿Tu historial crediticio es bueno? (si/no): " )
historial_crediticio = historial_crediticio.lower()
if historial_crediticio == "si" or historial_crediticio == "no":
    usuario["historial"] = historial_crediticio
else:
    print( "Ingrese unicamente 'si' o 'no'." )
    print( "Vuelve a ejecutar el programa." )
    exit()

# Deuda actual
print( "PORCENTAJE DE DEUDA ACTUAL" )
print( "Para calcular el porcentaje de deuda actual debes dividir la deuda ($$) para tus ingresos ($$) y multiplicar el resultado por 100" )
deuda_actual = input( "Ingresa tu porcentaje de deuda actual sobre tus ingresos: " )
if deuda_actual.isdigit():
    usuario["deuda"] = int(deuda_actual)
elif deuda_actual.find(".") != 1:
    deuda_actual_sin_punto = deuda_actual.replace(".", "", 1)
    if deuda_actual_sin_punto.isdigit():
        usuario["deuda"] = round(float(deuda_actual), 2)
    else:
        print( "El valor de porcentaje de deuda es incorrecto." )
        print( "Vuelve a ejecutar el programa." )
        exit()
else:
    print( "El valor de porcentaje de deuda es incorrecto." )
    print( "Vuelve a ejecutar el programa." )
    exit()

# Garantias
garantias = input( "¿Tienes alguna garantia como una propiedad? (si/no): " )
garantias = garantias.lower()
if garantias == "si" or garantias == "no":
    usuario["garantias"] = garantias
else:
    print( "Ingrese unicamente 'si' o 'no'." )
    print( "Vuelve a ejecutar el programa." )
    exit()

## Verificar la información obtenida

print( "\nPOR FAVOR VERIFICA SI TU INFORMACIÓN ESTÁ CORRECTA.\n" )
print( usuario )
print( "\n" )
info_ok = input( "¿Toda la información esta correcta? (si/no): " )
info_ok = info_ok.lower()
if info_ok == "no":
    print( "Vuelve a ejecutar el programa e ingresa bien la información." )
    exit()

## Verificar si cumple los requisitos para aprobación de credito

# Evaluar si cumple la mayoria de requisitos
if (usuario["ingresos"] > 30000 
    and usuario["historial"] == "si" 
    and usuario["edad"] >= 21 
    and usuario["edad"] <= 65 
    and usuario["deuda"] < 40):
    print( f"\n{usuario['nombre']} tu credito ha sido aprobado.\n" )

# Evaluar si hay excepciones basadas en garantias
elif (usuario["ingresos"] > 30000 or usuario["historial"] == "si") and (21 <= usuario["edad"] <= 65):
    if usuario["garantias"] == "si":
        print( f"\n{usuario['nombre']} tu credito ha sido aprobado debido a las garantias.\n" )
    else:
        print( f"\n{usuario['nombre']} tu credito no ha sido aprobado debido a falta de garantias.\n" )

# Rechazar si no cumple los requisitos
else:
    print( f"\n{usuario['nombre']} tu credito no ha sido aprobado.\n" )