"""Archivo para el scraper del BCV (Banco Central de Venezuela) que obtiene las tasas de cambio de divisas."""

import requests
from bs4 import BeautifulSoup
from typing import Optional

from app.core.divisas import Divisas
from app.settings.config import Config

class BCVScraper:
    """Scraper para extraer el valor de las divisas desde el sitio web del BCV."""

    def __init__(self):
        self.url = Config().URL_BASE
        self._soup = self._get_soup()

    def _get_soup(self) -> Optional[BeautifulSoup]:
        """Obtiene y parsea el HTML de la página del BCV."""
        try:
            response = requests.get(self.url, verify=False, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.text, "html.parser")
        except requests.RequestException as e:
            print(f"[BCVScraper] Error obteniendo la página del BCV: {e}")
            return None

    def _extraer_divisa_raw(self, divisa: Divisas) -> Optional[str]:
        """Extrae el valor crudo como texto de la divisa desde el HTML."""
        if not self._soup:
            return None

        div_container = self._soup.find("div", {"id": divisa.divisa()})
        if not div_container:
            print(f"[BCVScraper] No se encontró el contenedor para la divisa {divisa}")
            return None

        valor_div = div_container.find("div", {"class": "col-sm-6 col-xs-6 centrado"})
        if not valor_div:
            print(f"[BCVScraper] No se encontró la tasa para la divisa {divisa}")
            return None

        return valor_div.get_text(strip=True)

    def obtener_tasa(self, divisa: Divisas) -> Optional[float]:
        """Devuelve la tasa de la divisa como float si está disponible."""
        valor_crudo = self._extraer_divisa_raw(divisa)
        if not valor_crudo:
            return None

        try:
            return float(valor_crudo.replace(",", "."))
        except ValueError:
            print(f"[BCVScraper] Error parseando el valor '{valor_crudo}' para {divisa}")
            return None

    def obtener_todas(self) -> dict[Divisas, float]:
        """Devuelve un diccionario con todas las tasas disponibles."""
        tasas = {}
        for divisa in Divisas:
            tasa = self.obtener_tasa(divisa)
            if tasa is not None:
                tasas[divisa] = tasa
        return tasas