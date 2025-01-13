# OllamaProxy 🚀

**OllamaProxy** es un proxy inverso ligero y eficiente diseñado para redirigir solicitudes a la API de Ollama utilizando un túnel ngrok. Este proyecto es perfecto para desarrolladores que necesitan un puente entre su aplicación local y la API de Ollama, permitiendo una integración fluida y segura.

## Características principales 🌟

- **Multi-hilo**: Maneja múltiples solicitudes simultáneamente gracias a su arquitectura basada en hilos.
- **Flexible**: Soporta los métodos HTTP más comunes: GET, POST, PUT, DELETE y HEAD.
- **Fácil de usar**: Configuración rápida y sencilla, con opciones tanto interactivas como por línea de comandos.
- **Extensible**: Fácilmente adaptable para redirigir a cualquier servicio web.

## Instalación ⚙️

1. Clona el repositorio:

   ```bash
   git clone https://github.com/HirCoir/OllamaProxy.git
   cd OllamaProxy
   ```

2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

## Versión compilada para Windows 🖥️

Para aquellos que prefieren no lidiar con Python y sus dependencias, hemos preparado una **versión compilada** para Windows disponible en la sección [Releases](https://github.com/HirCoir/OllamaProxy/releases). Simplemente descarga el ejecutable y ¡estás listo para empezar!


## Uso 🛠️

### Modo interactivo

Simplemente ejecuta el script y sigue las instrucciones:

```bash
python OllamaProxy.py
```

### Modo con argumentos

Puedes especificar la URL de ngrok y el puerto directamente desde la línea de comandos:

```bash
python OllamaProxy.py --url https://tunombre.ngrok.io --port 11434
```

## Créditos 👏

Este proyecto fue desarrollado por **HirCoir**. Visita [hircoir.eu.org](https://hircoir.eu.org) para más información y otros proyectos interesantes.

## Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si tienes alguna idea, mejora o encuentras algún problema, no dudes en abrir un issue o enviar un pull request.

## Licencia 📜

Este proyecto está bajo la licencia MIT.
---

**¡Conéctate con nosotros!** 🌐

- [Sitio web](https://hircoir.eu.org)

---

**OllamaProxy** no solo es una herramienta, es tu puente hacia una integración más eficiente y segura con la API de Ollama. ¡Pruébalo hoy y lleva tu desarrollo al siguiente nivel! 🚀
