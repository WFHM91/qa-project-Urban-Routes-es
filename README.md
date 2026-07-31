# Proyecto Urban Routes - UI Test Automation Suite

---

## 1. Descripción
Este proyecto contiene una suite de pruebas automatizadas desarrolladas en Python para validar la interfaz de usuario (UI) y el flujo funcional completo de la plataforma web Urban Routes, específicamente enfocado en el proceso de reserva de un servicio de transporte (taxi).

El objetivo principal es verificar de forma automatizada que los componentes de la interfaz, botones, formularios interactivos y modales se comporten correctamente de acuerdo con las especificaciones de la aplicación. La suite abarca desde la selección inicial de direcciones de origen y destino hasta la asignación final del conductor, garantizando la correcta integración entre las selecciones del usuario y la respuesta del sistema.

---

## 2. Descripción de las Tecnologías y Técnicas Utilizadas

### Tecnologías:
* Python 3.x: Lenguaje de programación principal elegido por su sintaxis limpia, legibilidad y eficiencia en scripts de automatización.
* Pytest: Framework de pruebas de software utilizado para la organización, ejecución y generación de reportes detallados en consola.
* Selenium WebDriver: Herramienta de automatización web empleada para simular las acciones reales del usuario en el navegador (clics, escritura, scroll y lectura de propiedades CSS).

### Técnicas de Prueba Aplicadas:
* Page Object Model (POM): Patrón de diseño de software implementado para separar la representación de las páginas web (localizadores y métodos de acción) de la lógica de los casos de prueba, aumentando la reusabilidad y mantenibilidad del código.
* Pruebas de Extremo a Extremo (E2E): Estrategia de testing enfocada en evaluar el flujo completo de la aplicación de principio a fin, simulando la experiencia de un usuario real.
* Patrón AAA (Arrange-Act-Assert): Estructuración estándar aplicada a cada caso de prueba para dividir claramente la preparación del entorno/datos (Arrange), la ejecución de la acción (Act) y la validación de los resultados esperados (Assert).
* Sincronización Asíncrona (Explicit Waits): Uso de WebDriverWait y expected_conditions para gestionar la fluidez de la prueba frente a animaciones CSS y elementos de carga diferida en el DOM sin depender de pausas estáticas innecesarias.

---

## 3. Dependencias Necesarias
Para la correcta ejecución del proyecto, se necesitan las siguientes librerías de Python:
* pytest (Framework de gestión de pruebas)
* selenium (Librería de automatización web)

---

## 4. ¿Cómo instalar las dependencias?
Abre la terminal en la carpeta raíz de este proyecto y ejecuta el siguiente comando:

```bash
pip install pytest selenium
````
---

## 5. ¿Cómo ejecutar el proyecto?
Para correr todas las pruebas automatizadas y verificar los resultados de la suite en la consola, ejecuta el siguiente comando en la terminal:

```bash
python -m pytest tests/test_urban_routes.py -v
````