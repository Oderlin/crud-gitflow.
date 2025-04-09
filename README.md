# 🛒 Proyecto: Tienda Web con Automatización de Pruebas (Selenium)

Este proyecto es una tienda web básica con un carrito de compras funcional en modo demo (guardado en el navegador con `localStorage`) y una prueba automatizada con Selenium en Python que verifica la funcionalidad del buscador y el carrito.

# Estructura del Proyecto

tienda-automatizada/ index.html Página web de la tienda (modo demo) test_carrito.py Script de prueba automatizada con Selenium reporte.html  Reporte de prueba generado automáticamente /screenshots, Capturas automáticas durante la prueba. README.md, Documentación del proyecto.

# Requisitos

- Python 3.10+
- Navegador Google Chrome
- Selenium 4.6 o superior

# Instalación de dependencias

```bash
pip install selenium

# Ejecutar la prueba automatizada

    Abre una terminal o consola

    Ejecuta:

    python test_carrito.py

# Esto hará lo siguiente:

    Abre el archivo index.html local

    Busca "camisa" en la tienda

    Agrega el producto al carrito

    Abre el panel del carrito

    Toma una captura automática (/screenshots)

    Verifica que el producto esté en el carrito

    Genera un reporte HTML (reporte.html)

# Funcionalidades Automatizadas

    Buscar productos por nombre

    Agregar productos al carrito

    Ver contenido del carrito

    Validación con assert

    Capturas automáticas de pantalla

    Reporte de prueba en HTML

Historias de Usuario (Resumen)

    Buscar productos

    Agregar al carrito

    Ver carrito y vaciarlo

    Persistencia con localStorage

     Captura Automática

# Captura Automática

Una imagen del carrito abierto se guarda automáticamente en:

    /screenshots/carrito_abierto.png

# Demo Local

Para visualizar la tienda, abre index.html en tu navegador.

O ejecuta con un servidor local como:

python -m http.server

# Notas

    Este proyecto no realiza compras reales.

    El carrito y búsqueda funcionan en modo demo con JavaScript + localStorage.

    Ideal para prácticas QA y automatización de pruebas web.

# Autor

Oderlin Sanchez
Proyecto de demostración para prácticas de automatización con Selenium.
Incluye buenas prácticas, pruebas reales, reporte HTML, y organización limpia.
