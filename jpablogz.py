"""   TAREA 1
def darmensaje(mensaje):
    print("Hola mundo!")
    print(mensaje)
darmensaje("Función darmensaje") """

"""-----TAREA 2-----"""

# Se reciben los parametos de tipo texto, y el patron a buscar
def PatternCount(Text, Pattern):
    
# Se define un contador PatterCount
# Cada ocasión que ncuentra que el substring igual al patron
    cont = 0
    
# Se usan listas y tuplas que es la forma más sencilla de extraer caracteres individuales de cadenas (miembros individuales de cualquier secuencia)
    for i in range(0, len(Text) - len(Pattern) + 1):
        
# Se compara el substring con el patron dado y si es igual a la del contador
        if Text[i : len(Pattern) + i] == Pattern:
            cont += 1
    return print (cont)
PatternCount(input(), input());
