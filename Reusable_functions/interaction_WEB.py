# Se importa la clase Webdriver de la libreria selenium
from selenium import webdriver
# Se importa la clase ChromeService para poder pasar la ruta del chromedriver
from selenium.webdriver.chrome.service import Service as ChromeService
# Se importa la libreria que se encarga  e descargar automaticamente el chromedriver compatible con la versión del navegador chrome
from webdriver_manager.chrome import ChromeDriverManager
# Se importa una clase de la libreria selenium que ayuda a la búsqueda de elementos en Web HTML
from selenium.webdriver.common.by import By

class ejecutar_chrome:

    # Se define el método constructor o de inicialización de la clase
    def __init__(self):
        # Se controla la ejecución del código con try-except para controlar posibles errores
        try:
            # Obtener la ruta del ejecutable de ChromeDriver automáticamente tras realizar la descarga de la versión correspondiente
            chrome_driver_path = ChromeDriverManager().install()

            # Ruta al ejecutable de ChromeDriver informada de forma manual
            #chrome_driver_path = r'C:\PYTHON\Automation\automation\Chrome\chromedriver.exe'

            # Configuración de opciones del navegador (opcional)
            chrome_options = webdriver.ChromeOptions()

            # Puedes agregar opciones, por ejemplo, para ejecutar en modo incógnito:
            #chrome_options.add_argument('--incognito')

            # Crear una instancia del servicio ChromeDriver
            chrome_service = ChromeService(executable_path=chrome_driver_path)

            # Crear una instancia del navegador Chrome con el servicio y las opciones
            driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

            # Ejemplo: abrir una página web
            driver.get('https://www.thesun.co.uk/sport/football/')

            # Realizar otras operaciones con Selenium...
            #element = driver.find_element(By.XPATH, value=r'//*[@id="customiser-v2-13503409"]/div[2]/div/div[1]/div/div[2]/a/p')
            element = driver.find_element(By.XPATH, value=r'//div[@class="teaser__copy-container"]/a/h3')

            print(element.text)


            # Cerrar el navegador al finalizar
            driver.quit()


        # Se trata el error obtenido
        except Exception as e:
            # Se imprime el error obtenido
            print(f'No se pudo abrir el chromedriver: {e}')
