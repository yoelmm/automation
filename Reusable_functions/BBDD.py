import mysql.connector
import pyodbc

class Gestion_BBDD:

    #Método constructor de la clase
    def __init__(self, entorno):

        if entorno == 'TOOLS':
            # Configura la conexión a la base de datos
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Welcome123"
            )

            # Crea un objeto cursor para interactuar con la base de datos
            cursor = conexion.cursor()

            # Ejecuta una consulta
            cursor.execute("SELECT * FROM bdemployees.departments")

            # Obtiene los resultados
            resultados = cursor.fetchall()

            # Itera sobre los resultados e imprímelos
            for fila in resultados:
                print(fila)

            # Cierra el cursor y la conexión
            cursor.close()
            conexion.close()

        if entorno == 'BBDD_CLIENTE':
            # Especifica los detalles de la conexión
            driver = 'ODBC Driver 18 for SQL Server'
            server = 'LAPTOP-DT5JG5J0'
            database = 'GNF_ELEC'
            username = 'sa'
            password = 'Welcome123'

            # Crea la cadena de conexión
            connection_string = (
                f'DRIVER={driver};'
                f'SERVER={server};'
                f'DATABASE={database};'
                f'UID={username};'
                f'PWD={password};'
            )

            # Intenta establecer la conexión
            try:
                connection = pyodbc.connect(connection_string)
                print('Conexión exitosa')

                # Aquí puedes realizar operaciones en la base de datos

                # No olvides cerrar la conexión cuando hayas terminado
                connection.close()

            except pyodbc.Error as e:
                print(f'Error en la conexión: {e}')



