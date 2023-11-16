# La variable especial __name__ en python permite determinar si el fichero de python que se ejecuta es el programa principal
# El fichero que se establece como programa principal de ejecución asigna el siguiente valor a la variable especial __name__='__main__'
from Reusable_functions import BBDD
if __name__ == '__main__':
    print('Hola Mundo')
    BBDD.Gestion_BBDD()