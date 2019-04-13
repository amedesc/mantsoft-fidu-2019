"""Primera tarea del proyecto practico"""
def darmensaje(mensaje):
    print("Hola mundo!!",mensaje)

darmensaje("Pura vida!!")

"""Segundo tarea del proyecto practico"""
"""Esta funcion lo que realiza es un analisis
de las coincidencias que se pueden encontrar en un texto
segun el pattern o la caracteritica que se quiera rastrear
para este ejemplo utilice mis nickname y realice una busqueda 
de coincidencia con las iniciales de mi nombre obteniendo una
salida de 4 coincidencias en algunos de mis nickname"""
def PatternCount(text, pattern):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        if text[i: len(pattern) + i] == pattern:
            count = count + 1
    print(count)

PatternCount("KAREN_KAII_KA_MACHA_VANE_KARL","KA")