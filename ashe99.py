"""def darmensaje(mensaje):
    print ("Hola Mundo!!!", mensaje)

darmensaje("Buenas Profe")"""

#Science Data

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)):

        if Text[i:i+len(Pattern)] == Pattern: 
            count+=1
    return count

Text = "GCGCGCG"
Pattern = "GCG"
print(PatternCount(Text, Pattern))

"""La declaración if lo que busca hacer es ver si el valor del índice i en el texto es igual al índice 0 en el patrón (que es G).
si encuentra una G en el texto, verificará si del índice i al índice i + la longitud del patrón (es i + la longitud del patrón (3)
porque se detiene una vez que alcanza i + 3 y No incluye el valor de Texto [i + 3] por lo tanto, solo será i, i + 1 e i + 2) y 
si coincide con el patrón"""
