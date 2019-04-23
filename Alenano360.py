#Semana 1
def darmensaje(mensaje):
    print ("Hola Mundo", mensaje, ".")

darmensaje("ALEJANDRO")



#Semana 2
#la variable cadena es la el string que se analisa en la funcion
Cadena="CCCATTAATATTAGCACCTGCCGACTAGCTGCCGACGTAACCCGTTATCCTGCCGAGGCTGCCGAATAGACTGCCGACGGTGTCTGCCGAAGAGTTCTGGTCCTGCCGACCTGCCGACCTGCCGAGAACTGCCGAGCACTGCCGACTGCCGAACTGCCGATACGATGGATCTGCCGACTTACTATGCAACCTGCCGACTGCCGACGCCCTGCCGACCACCTGCCGACTGCCGATCTGCCGAACACGGCGCTGCCGATCCTGCCGAGTCTGCCGACTGCCGATACTGCCGAGCCTGCCGATTCTGCCGACTGCCGATACATGTCCTGCCGACTTTACTGCCGAGCACTAAGGACTGCCGACTGCCGAAAATGAGTCGTCTGCCGACCAGCTGCCGACCTGCCGACTGCCGACTAATCTGCCGACTGCCGACTGCCGACTCCTGCCGATTTCAAAGGGTGCAACTGCCGACCTGCCGACTGCCGAGATGCTGCCGATACTCTGCCGAAACTCTGCCGATCAGTTGACACTGCCGACACTGCCGAACTGCCGACATTTCTGCCGACTCATCTGCCGAGCTGCCGACTGCCGACCACGCTGCCGACCTCTGCTGCCGAGGTATCCTGCCGAGTCACAACTGCCGAACTGCCGACCTGCCGATGCTGCCGATCTCCTGCCGAATTGACTGCCGACTGATATAGACTGCCGATCGGCAGTTCCTCTGCCGATCTGCCGAGCCTGCCGAATGGGACGCTGCCGACTCTGCCGAGATGTAGGCTGCCGATCGATCTGCCGAGGCTGCCGAGAGCCTGCCGACGCCTGCCGACTGCCGAATCTGCCGACTGCCGAAACCGGGGCCACTGCCGATGCGTCTGCCGATTTACTGCCGACTGCCGATCACGCTCTGCTGCCGACTGCCGATGCCTGCCGATCTGCCGAT"
#la variable patron es el subtring que se repite dentro de la variable cadena
Patron="CTGCCGACT"
#la funcion numeroPratrones recibe las variables anteriores para identificar la cantidad de veces que se encuentra el subtring en el string
def numeroPratones(Cadena, Patron):
    #la variable conta es el contador que lleva la cantidad de veces que se repide el substring
    conta = 0
    #se empieza a recorrer la cadena de texto
    for i in range(0, (len(Cadena) - len(Patron) + 1)):
        #se pregunta si la cadena en la posicion n es igual al patron
        if Cadena[i:i+len(Patron)] == Patron:
            #si cumple al contador se le suma uno 
           conta = conta + 1 
           #se imprime el valor de conta que seria el numero de veces que se repite el substring en el string
    print("El numero veces que repite el patron es:",conta)

numeroPratones(Cadena,Patron)
