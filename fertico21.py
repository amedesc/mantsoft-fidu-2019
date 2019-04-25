
# Esta función concatena 2 cádenas de texto
# Recibe como parametro un mensaje y retorna "Hola mundo" + mensaje enviado
def darmensaje(mensaje): 
    print ("Hola mundo!", mensaje)

darmensaje("Fernando")

# Esta Función determina la frecuencia con la que un patrón aparece en una cadena de texto
# Recibe como parámetros el texto y el patrón. Y retorna el número de veces que se encuentra ese patrón en el texto
def PatternCount(texto, patron):
    contador = 0
    for x in range(0, len(texto)):
        if texto[x:len(patron)+x] == patron:
            contador += 1
    return contador

a = PatternCount("ADNABCDEFGHIJKLMNOPQRSTUWXYZADNABCDEFGHIJKLMNOPQRSTUWADNXYZADNABCDEFGHIJKLMNOPQRSTUWXYZADNADN","ADN")
print (a)

