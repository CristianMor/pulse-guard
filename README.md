# 🛠️ modfile-py-renamer

Bienvenido a modfile-py-renamer! 👋 Esta es una herramienta de línea de comandos (CLI) diseñada para hacer la gestión de archivos mucho más sencilla y rápida. 🎯 Con esta aplicación, puedes renombrar archivos en una carpeta específica eliminando ciertas partes del nombre.

## 📄 ¿Qué hace?

Esta primera versión de modfile-py-renamer te ayuda a renombrar archivos en una carpeta, eliminando patrones innecesarios en el nombre de los archivos. Si tienes archivos con nombres como:

`003_0810232324_Rms_upd.txt`

La aplicación los renombrará a:

`003_08102323_Rms.txt`

## 🚀 Funcionalidades Principales

- Renombra archivos en una carpeta específica.
- Elimina los últimos dos dígitos del bloque de números.
- Elimina sufijos no deseados como "_upd" antes de la extensión del archivo.
- Usa colores y emojis para una experiencia amigable y agradable. 🎨

## 🧑‍💻 ¿Cómo usarla?
1. **Clona el repositorio**:
```bash
git clone https://github.com/CristianMor/modfile-py-renamer.git
```

2. **Navega a la carpeta del proyecto**:
```bash
cd modfile-py-renamer
```

3. **Instala las dependencias**:

Asegúrate de tener instaladas las librerías necesarias (click y rich), puedes hacerlo usando el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

4. **Selecciona una opción**:
- **Renombrar archivos**: La CLI te pedirá que ingreses la ruta de la carpeta que contiene los archivos a renombrar.
```bash
python -m modfile_py_renamer.cli renombrar
```

```bash
python -m modfile_py_renamer.cli
```

## ✨ Características
- Renombra archivos eliminando partes innecesarias de sus nombres de forma rápida.
- Usa un diseño minimalista con colores y emojis para mejorar la experiencia de usuario. 🎨
- Fácil de configurar y usar. 😄


## 🛠️ Requisitos
- Python 3.11.1 🐍
- Librerías: click y rich (instaladas automáticamente con requirements.txt)

## 🚧 Próximas Funcionalidades:

- Soporte para múltiples tipos de archivos y extensiones.

## 🎯 Contribuir

Si te interesa mejorar o agregar más funcionalidades a modfile-py-renamer, ¡las contribuciones son bienvenidas! 🤝 Puedes crear un fork del proyecto, hacer tus mejoras y enviar un pull request.

¡Gracias por usar modfile-py-renamer! ✨
