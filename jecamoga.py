#Hola mundo
def darmensaje (mensaje):
    print (mensaje)


darmensaje("Hola mundo!")


#Funcion PatternCount
def PatternCount(Text, Pattern):
    count = 0
    for i in range(0, (len(Text) - len(Pattern) + 1)):
        if Text[i:i+len(Pattern)] == Pattern:
       		count = count + 1
    return count

#En este Input se coloca la cadena a leer
Input = "GCGCG"

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
            
#Este print obtiene cuántas veces se repite el pattern
    print (maxcount)   
    return maxpattern

#Este print obtiene el pattern que se repite tres veces,
#ya que el número 3 define la cantidad de letras que deben repetirse.
print (FrequentWords(Input, 3))
