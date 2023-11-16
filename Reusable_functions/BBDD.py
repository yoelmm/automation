import mysql.connector

class Gestion_BBDD:
    def __init__(self):

        # Configura la conexión a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Welcome123",
            database="bdemployees"
        )

        # Crea un objeto cursor para interactuar con la base de datos
        cursor = conexion.cursor()

        # Ejecuta una consulta
        cursor.execute("SELECT * FROM departments")

        # Obtiene los resultados
        resultados = cursor.fetchall()

        # Itera sobre los resultados e imprímelos
        for fila in resultados:
            print(fila)

        # Cierra el cursor y la conexión
        cursor.close()
        conexion.close()

