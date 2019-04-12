#Entregable 1

def darmensaje(mensaje):
    print("Hola Mundo")
    print(mensaje)
darmensaje("Funcion darmensaje")


#Entregable 2

# EL codigo va determinar la frecuencia con la que un patrón aparece en una cadena de texto.
# se va a Recibir como parámetros el texto y el patrón. Y retorna el número de veces que se encuentra ese patrón en el texto en este caso tiene que imprimir ADN y sus repeticiones.

def PatternCount(Text, Pattern):
    count = 0
    for i in range(0, (len(Text) - len(Pattern) + 1)):
        if Text[i:i+len(Pattern)] == Pattern:
       		count = count + 1
    return count


Input = "XYZADNADNXYADNZXYZXYZXYZXYZADNADNXYZXADNYADNZXADNYZXYADNZXYZ"

def FrequentWords(Text, x):
    maxcount = 0
    patternlength = int(x)
    maxpattern = []
    for i in range(0, (len(Text) - patternlength + 1)):
        if PatternCount(Text, Text[i:i + patternlength]) > maxcount:
            maxcount = PatternCount(Text, Text[i:i+patternlength])
            maxpattern = []
            maxpattern.append(Text[i:i + patternlength])
        elif PatternCount(Text, Text[i:i + patternlength]) == maxcount and Text[i:i+patternlength] not in maxpattern:
            maxpattern.append(Text[i:i + patternlength])

    print ("El patron se repite", maxcount, "veces")   
    return maxpattern
print ("El patron es", FrequentWords(Input, 3))
