from telegram import Update
from telegram.ext import ContextTypes

from app.app_log import get_logger
from app.core import Divisas, BCVScraper
from app.settings import Config

logger = get_logger(f"[{Config().APP_NAME}: Command Module]")

async def lira(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        scraper = BCVScraper()
        precio = scraper.obtener_tasa(Divisas.LIRA)
        logger.info(f"Enviando precio de {Divisas.LIRA.value}")
        await update.message.reply_text(f"El precio del {Divisas.LIRA.value} es: {str(precio)}")
    except Exception as e:
        logger.error(f"Error al enviar el precio del {Divisas.LIRA.value}: {e}")