💰 BCV Divisas Bot 

![Python](https://img.shields.io/badge/Python-3.12%252B-blue?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram)
![BCV](https://img.shields.io/badge/BCV-API-yellow)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Code Style](https://img.shields.io/badge/code%2520style-black-000000.svg)

> Bienvenido al repositorio de **BCV Divisas Bot**, un bot de Telegram diseñado para ofrecerte tasas de cambio de divisas en tiempo real.

Este bot se conecta a la API del Banco Central de Venezuela (BCV) para obtener la información más actualizada y la presenta de manera simple y accesible directamente en tus chats de Telegram.

## ✨ Características

- **Consultas en Tiempo Real:** Obtén tasas de cambio actualizadas para diversas divisas.
  
- **Interacción Sencilla:** Usa comandos intuitivos para solicitar información de divisas específicas.

- **Logging Detallado:** Un sistema de registro robusto que monitorea la actividad del bot y facilita la depuración.

- **Configuración Flexible:** Personaliza el comportamiento del bot a través de variables de entorno.

- **Arquitectura Modular:** Código organizado en módulos lógicos para una mejor mantenibilidad.

### 📋 Requisitos

> Para ejecutar Telegram Currency Bot, necesitarás lo siguiente:

- **Python 3.12+**
- **Un token de bot de Telegram** (obtenido de BotFather)

#### Dependencias de Python

Las dependencias están listadas en `requirements.txt`:

- python-telegram-bot
- requests
- python-dotenv

```bash
# Clona el repositorio (o descarga los archivos del proyecto)
git clone https://github.com/anjivervas/luigi_bcv
cd bcv-divisas-bot

# Crea un entorno virtual (recomendado) e instálalo:
python -m venv venv

# En Windows:
.\venv\Scripts\activate

# Instala las dependencias del proyecto:
pip install -r requirements.txt
```

## ⚙️ Configuración

#### Sigue estos pasos para configurar y poner en marcha el bot:

- Clona el repositorio (o descarga los archivos del proyecto).

#### Configura el archivo `.env`
Crea un archivo llamado **`.env`** en la raíz de tu proyecto con el siguiente contenido:

```
TELEGRAM_BOT_KEY="TU_TOKEN_DE_TELEGRAM_AQUI"
LOG_LEVEL="INFO" # Puedes cambiar a DEBUG, WARNING, ERROR
```

> ⚠️ **Nota:** Asegúrate de no compartir tu token de Telegram.

1. Reemplaza `TU_TOKEN_DE_TELEGRAM_AQUI` con el token proporcionado por BotFather.
2. Ajusta `LOG_LEVEL` según tus necesidades.

## 🚀 Comandos Disponibles

Una vez que el bot esté en funcionamiento, puedes interactuar con él en Telegram usando los siguientes comandos:

- `/start`: Inicia la conversación con el bot y recibe un mensaje de bienvenida.
- `/dolar`: Obtiene la tasa actual del Dólar.
- `/euro`: Muestra el valor del Euro.
- `/lira`: Consulta la tasa de la Lira.
- `/rublo`: Proporciona el valor del Rublo.
- `/yuan`: Devuelve la tasa actual del Yuan.

## 💬 Ejemplo de Uso

Para obtener la tasa de cambio, simplemente abre un chat con el bot en Telegram y envía el comando correspondiente. Por ejemplo:

```bash
# Inicia el bot y envía un mensaje de bienvenida.
/start

# El bot responderá con la tasa actual del Dólar.
/dolar
```

## 📂 Estructura del Proyecto

```
luigi_bcv/
├── app/                    # Contiene el código fuente
│   ├── app_log/            # Módulo para la configuración y gestión logging
│   │   ├── __init__.py     # Permite importar sus módulos
│   │   ├── log_config.py   # Archivos y controladores
│   │   └── logger.py       # Obtiene instancias de logger
│   ├── bot/                # Lógica central del bot de telegram
│   │   ├── __init__.py     # Exporta la función principal del bot
│   │   ├── bot             # Configura los manejadores de comandos y lo pone en funcionamiento
│   │   └── commands/       # Contiene comandos de cada divisa
│   ├── core/               # Contiene la lógica principal
│   │   ├── __init__.py     # Exporta las clases Horoscopo y signos
│   │   ├── divisas.py      # Define la clase divisas
│   │   └── scraper.py      # Define una enumeración
│   ├── settings/           # Módulo para la gestión de configuración
│   │   ├── __init__.py     # Exporta la clse config
│   │   └── config          # Contiene las variable config
│   └── __init__.py         # Impota el módulo de nivel superior (bot) para run.py
├── .env                    # Almacena las variables de entorno sesibles
├── .gitignore              # Especifica que archivo/carpeta deben ser ignorados
├── docker-compose.yml      # Define múltiples servicios (contenedores) de la aplicación, cada uno con su propia configuración
├── Dockerfile              # Especifica el sistema operativo base y las dependencias necesarias para ejecutar la aplicación
├── README                  # Archivo de documentación
├── requirements            # Lista de las dependencias de python
├── run.py                  # Script principal para la ejcución del bot
```

Cuando envías un comando, el bot te devolverá un mensaje con la tasa de cambio obtenida de la API.

> La respuesta incluirá un mensaje de la moneda y el valor de la divisa.

🏁 **¡Espero que disfrutes usando BCV Divisas Bot!** 

## 📄 Licencia

MIT © [Luigi Delgado](https://github.com/LUIGIJDM)
