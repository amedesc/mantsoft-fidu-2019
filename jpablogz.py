"""Tarea #1
def darmensaje(mensaje):
    print("Hola mundo!")
    print(mensaje)
darmensaje("Función darmensaje")"""


#Tarea #2

# Funcion para determinar cuentas veces se repite una cadena de texto dentro de otra
# Recibe dos parametros tipo texo y el patron a buscar 
def PatternCount(Text, Pattern):
    
# Se declara un un contador, PatternCount para llevar el conteo 
# Cada vez que encuentre que el substring igual al patron
    cont = 0
    
# Uso una listas y tupla para extraer caracteres individuales de cadenas (miembros individuales de cualquier secuencia)
    for i in range(0, len(Text) - len(Pattern) + 1):
        
# Se hace la comparacion del substring con el patron ingresado  y si se iguala a la suma del contrador
        
    if Text[i : len(Pattern) + i] == Pattern:
            cont += 1
    return print (cont)
PatternCount(input(), input());
