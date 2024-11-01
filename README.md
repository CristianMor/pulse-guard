# 🛠️ Pulse Guard 

```plaintext                                                     
,---.     |                                         |
|---'.   .|    ,---.,---.   ,---..   .,---.,---.,---|
|    |   ||    `---.|---'---|   ||   |,---||    |   |
`    `---'`---'`---'`---'   `---|`---'`---^`    `---'
                            `---'                    
```
Bienvenido a **pulse-guard**! 👋 Esta es una herramienta de línea de comandos (CLI) diseñada para facilitar el monitoreo y la corrección de archivos en el sistema crítico de *Acuicultec.com* que dependen del procesamiento de datos de sonido. 🚀

## 📄 ¿Qué hace?

**pulse-guard** se encarga de:

- **Monitorear archivos**: Inspecciona archivos de datos generados por el sistema, identificando datos faltantes o problemas que podrían comprometer la integridad del flujo de información.
- **Corregir errores**: Proporciona soluciones automáticas para corregir problemas, como renombrar archivos para permitir la decodificación correcta y asegurar que todos los datos estén en el formato esperado.
- **Simplificar el mantenimiento**: Ofrece una interfaz interactiva que permite a los usuarios verificar y corregir archivos sin necesidad de comandos complejos, haciendo que las tareas de monitoreo sean más simples y rápidas.

## 🚀 Funcionalidades Principales

- **Menú interactivo**: 🤖 Un menú fácil de usar que guía al usuario a través de las opciones disponibles para verificar y corregir archivos.
- **Renombrar archivos RMS**: ✏️ Una función que renombra archivos de sonido RMS para permitir su correcta recodificación.
- **Verificar datos faltantes**: 🕵️‍♂️ Un comando que analiza los archivos de datos de sonido y detecta cualquier dato faltante, asegurando que no haya brechas en la información procesada.

## 🧑‍💻 ¿Cómo usarla?
1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/CristianMor/pulse-guard.git
    ```

2. **Navega a la carpeta del proyecto**:

    ```bash
    cd pulse-guard 
    ```

3. **Instala las dependencias**:

    Asegúrate de tener instaladas las librerías necesarias, puedes hacerlo usando el archivo requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**:

    - Renombra el archivo .env-example a .env:


    ```bash
    mv .env-example .env
    ```

    - Abre el archivo .env y configura las rutas necesarias para las carpetas de entrada y salida.

## 📋 Ejemplo de uso

Para ejecutar un comando básico de verificación de data faltante por procesar, usa:

```bash
pulse-guard verify-data
```

Esto iniciará el proceso de verificación y mostrará los archivos que faltan por procesar.

### Usar el menú interactivo

Para acceder al menú interactivo y explorar las opciones de verificación y correción:

```bash
pulse-guard interactive
```

El menú interativo te permitirá seleccionar acciones de manera fácil y directa. 🤖

## 🛠️ Requisitos
- Python 3.12.4 🐍
- Librerías: 
    - click 
    - rich 
    - python-dotenv
    - inquirer
    - yaspin

## 🚧 Próximas Funcionalidades:

- Soporte para múltiples tipos de archivos y extensiones.

## 🎯 Contribuir

¡Las contribuciones son bienvenidas! 🎉 Si tienes ideas o mejoras, no dudes en hacer un fork del proyecto, agregar tus cambios y enviar un pull request.

¡Gracias por usar pulse-guard! ✨
