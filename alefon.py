'''
Semana pasada

 def darmensaje(mensaje):
    print("Hola mundo "+ mensaje +"!")

def  crearmensaje():
    mensaje = input("Ingrese algún texto : ")
    darmensaje(mensaje)
    nuevomensaje()

def nuevomensaje():
        opt = input("Desea enviar otro mensaje? Y/N : ")
        if opt == "Y" or opt == "y":
            crearmensaje()
        elif opt == "N" or opt == "n":
            print("Adios!")
        else:
            print("Valor inválido, vuelva a intentarlo")
            nuevomensaje()


crearmensaje()


'''
import re
import os.path

#función para contar patrones, recibe como parámetros un patrón y un archivo de texto.

def PatternCount(file,pattern):
    patternAlter = pattern[:2]+ "]|" + pattern[2:]
    # matches obtiene el valor de la búsqueda de iteraciones de el patrón recibo en el texto recibido
    matches = re.finditer(patternAlter, file.read(), re.MULTILINE | re.IGNORECASE)
    # se cuentan las iteraciones
    for matchC, match, in enumerate(matches, start = 1):

        matchC = matchC
    #finalmente se imprimen el conteo de iteraciones
    result = print("The pattern ", pattern, " was found ", matchC, " times on the file.")

    return result

# función que muestra el menú de este script
def menu():
    # aquí obtenemos la ruta absoluta de este archivo
    path = os.path.abspath(os.path.dirname(__file__))
    # aquí se unen la ruta de este archivo o script  con la del archivo que estamos buscando
    fileP = os.path.join(path,input("Please provide the file route and name :"))
    # se puede ingresar un patrón deseado
    pattern = input("Please enter the desired pattern (if empty the pattern will be CTGCCGACT) :")
    # se intenta ejecutar la acción de abrir el archivo y además se verifica si el patrón está vacío, para asignar un valor por defecto
    # en caso de que algo falle, se imprime la excepción en pantalla (si algo falla en pattern count, la excepción también lo captura)
    try:

        file = open(fileP)
        if pattern == "":
            pattern = "CTGCCGACT"
        PatternCount(file,pattern)
    except Exception as e:
        print(e)
        menu()
menu()
