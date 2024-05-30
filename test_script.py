import undetected_chromedriver as uc

# Inicializar el navegador
driver = uc.Chrome()

# Abrir una página web
driver.get('https://www.example.com')

# Interactuar con la página (ejemplo: imprimir el título de la página)
print(driver.title)

# Cerrar el navegador
driver.quit()