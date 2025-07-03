from telegram import Update
from telegram.ext import ContextTypes

from app.app_log import get_logger
from app.core import Divisas
from app.settings import Config

logger = get_logger(f"[{Config().APP_NAME}: Command Module]")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = f"""
¡Hola! Soy *{Config().APP_NAME}*, un bot creado por *{Config().AUTHOR_NAME}* como proyecto para la materia Transmisión de Datos.

Mi trabajo es proporcionarte el valor de la tasa del día que da el BCV para cualquiera de estas divisas:

    • {Divisas.DOLAR.description}: /{Divisas.DOLAR.value}
    • {Divisas.EURO.description}: /{Divisas.EURO.value}
    • {Divisas.LIRA.description}: /{Divisas.LIRA.value}
    • {Divisas.RUBLE.description}: /{Divisas.RUBLE.value}
    • {Divisas.YUAN.description}: /{Divisas.YUAN.value}

¿Cuál divisa quisieras consultar?
    """
    # Enviar el mensaje de bienvenida al usuario
    await update.message.reply_text(welcome_text, parse_mode='Markdown')
    logger.info("Enviado mensaje de bienvenida al usuario")