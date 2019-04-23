# Primer ejercicio 
def darMensaje(mensaje):
	saludo = 'Hola mundo, bienvenido a Python. '+mensaje
	print (saludo)


#darMensaje("Este es el mensaje de prueba")
               
# Segundo ejercicio

# La función recibe por parámetro 2 argumentos de tipo sring.
# Usamos la función string slicing de python para preguntar si desde la posición "i" del string coincide con el largo del patrón que mandamos por parámetro, en caso que la condición se cumpla, aumentamos en 1 el contador para posteriormene imprimir el resultado.
# Devuelve la cantidad de veces que se encontró el patrón en el texto analizado.

pattern = "GCG" 
text = "GCGCG" 

def contarPatrones(text, pattern): 
    count = 0 
    for i in range(0, len(text) - len(pattern) + 1): 
        if text[i : len(pattern) + i] == pattern: 
            count += 1 
    return print(count) 

contarPatrones(text, pattern) 

# Reto adicinal
adn = "CCCATTAATATTAGCACCTGCCGACTAGCTGCCGACGTAACCCGTTATCCTGCCGAGGCTGCCGAATAGACTGCCGACGGTGTCTGCCGAAGAGTTCTGGTCCTGCCGACCTGCCGACCTGCCGAGAACTGCCGAGCACTGCCGACTGCCGAACTGCCGATACGATGGATCTGCCGACTTACTATGCAACCTGCCGACTGCCGACGCCCTGCCGACCACCTGCCGACTGCCGATCTGCCGAACACGGCGCTGCCGATCCTGCCGAGTCTGCCGACTGCCGATACTGCCGAGCCTGCCGATTCTGCCGACTGCCGATACATGTCCTGCCGACTTTACTGCCGAGCACTAAGGACTGCCGACTGCCGAAAATGAGTCGTCTGCCGACCAGCTGCCGACCTGCCGACTGCCGACTAATCTGCCGACTGCCGACTGCCGACTCCTGCCGATTTCAAAGGGTGCAACTGCCGACCTGCCGACTGCCGAGATGCTGCCGATACTCTGCCGAAACTCTGCCGATCAGTTGACACTGCCGACACTGCCGAACTGCCGACATTTCTGCCGACTCATCTGCCGAGCTGCCGACTGCCGACCACGCTGCCGACCTCTGCTGCCGAGGTATCCTGCCGAGTCACAACTGCCGAACTGCCGACCTGCCGATGCTGCCGATCTCCTGCCGAATTGACTGCCGACTGATATAGACTGCCGATCGGCAGTTCCTCTGCCGATCTGCCGAGCCTGCCGAATGGGACGCTGCCGACTCTGCCGAGATGTAGGCTGCCGATCGATCTGCCGAGGCTGCCGAGAGCCTGCCGACGCCTGCCGACTGCCGAATCTGCCGACTGCCGAAACCGGGGCCACTGCCGATGCGTCTGCCGATTTACTGCCGACTGCCGATCACGCTCTGCTGCCGACTGCCGATGCCTGCCGATCTGCCGAT"
patron = "CTGCCGACT"
contarPatrones(adn, patron) # llamamos a la función de nuevo para calcular el reto adicional cuyo resultado es 23.




               



               
