#Oderlin Sanchez
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Abre Chrome automáticamente con Selenium Manager
driver = webdriver.Chrome()

# Abre el archivo HTML local
archivo = os.path.abspath("index.html")
driver.get(f"file:///{archivo}")
driver.maximize_window()

time.sleep(2)

# Buscar un producto
buscador = driver.find_element(By.ID, "searchInput")
buscador.send_keys("camisa")
time.sleep(2)

# Agregar producto al carrito
boton_agregar = driver.find_element(By.XPATH, "//button[contains(text(),'Agregar al carrito')]")
boton_agregar.click()
time.sleep(1)

# Abrir el carrito
carrito = driver.find_element(By.XPATH, "//button[contains(.,'🛍️')]")
carrito.click()
time.sleep(2)

# Tomar captura
os.makedirs("screenshots", exist_ok=True)
driver.save_screenshot("screenshots/carrito_abierto.png")

# Verificar que el carrito contiene el producto
contenido = driver.find_element(By.ID, "cartItems").text
assert "Camisa Blanca" in contenido, " El producto no se agregó al carrito correctamente."

# Guardar reporte HTML básico
with open("reporte.html", "w") as f:
    f.write("<h1> Resultado de la Prueba</h1>")
    f.write("<p> Prueba ejecutada con éxito</p>")
    f.write('<img src="screenshots/carrito_abierto.png" width="400"/>')

# Finalizar prueba
driver.quit()