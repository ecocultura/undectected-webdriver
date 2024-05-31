import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Establecer la variable de entorno para usar el display virtual
os.environ['DISPLAY'] = ':1'

# Configurar las opciones de Firefox
options = Options()
#options.headless = True  # Ejecutar en modo headless (sin interfaz gráfica)



# Configurar el servicio de geckodriver
service = Service('/usr/local/bin/geckodriver')

try:
    # Inicializar el navegador Firefox con las opciones y el servicio
    driver = webdriver.Firefox(service=service, options=options)

    # Abrir una página web
    driver.get('https://www.youtube.com')

    # Esperar hasta que el campo de búsqueda esté visible e interactuable
    wait = WebDriverWait(driver, 60)  # Incrementar el tiempo de espera
    inputbuscar_yt = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]')))

    
    # Buscar la banda "Epica" en YouTube
    banda = "Epica"
    inputbuscar_yt.send_keys(banda)
    
    # Esperar a que aparezcan los resultados de búsqueda y hacer clic en el botón de búsqueda
    botonbuscar_yt = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="search-icon-legacy"]')))
    botonbuscar_yt.click()
    print("hasta aqui todo funciona...")

    # Esperar a que la página se cargue completamente
    time.sleep(65)  # Agregar una espera implícita (puede ajustarse según la velocidad de carga de la página)



    # Intentar obtener los títulos de los videos encontrados
    try:
    # Esperar a que se carguen todos los elementos de los videos
        videos_yt = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[starts-with(@id, "video-title")]')))
        videos_titulos = [i.get_attribute('title') for i in videos_yt]
        if videos_titulos:
            print(videos_titulos)
        else:
            print("No se encontraron títulos de videos.")
    except TimeoutException:
        print("Tiempo de espera excedido. Los elementos 'video-title' no se encontraron.")

except TimeoutException:
    print("Tiempo de espera excedido al intentar cargar la página inicial.")
except Exception as e:
    print(f"Error Type: {type(e).__name__}")
    print(f"Error Message: {e}")


    '''# Interactuar con la página (ejemplo: imprimir el título de la página)
    print(driver.title)
    time.sleep(130)

    banda = "epica"
    inputbuscar_yt = driver.find_element(by=By.ID, value = "search")
    inputbuscar_yt.send_keys(banda)
    botonbuscar_yt = driver.find_element(by=By.ID, value = "search-icon-legacy").click()
    videos_yt = driver.find_elements(by=By.ID, value = "video-title")
    videos_yt = [i.get_attribute('title') for i in videos_yt]
    print(videos_yt)
'''
# Esperar unos segundos para ver el resultado (opcional)
    webdriver.implicitly_wait(5)



