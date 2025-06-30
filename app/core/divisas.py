"""Lista de divisas soportadas por el BCV."""

from enum import StrEnum

class Divisas(StrEnum):
    """Enum que representa las divisas soportadas por el BCV."""
    DOLAR = "dolar"
    EURO = "euro"
    YUAN = "yuan"
    LIRA = "lira"
    RUBLE = "rublo"

    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Divisas.{self.name}"
    
    @property
    def description(self) -> str:
        """Devuelve una descripción legible de la divisa."""
        return {
            Divisas.DOLAR: "Dólar estadounidense",
            Divisas.EURO: "Euro",
            Divisas.YUAN: "Yuan chino",
            Divisas.LIRA: "Lira turca",
            Divisas.RUBLE: "Rublo ruso"
        }.get(self, "Divisa desconocida")

    
    def divisa_id(self) -> str:
        """Devuelve el identificador de la divisa en minúsculas."""
        return self.name.lower()
    
    def divisa(self) -> str:
        """Devuelve el nombre de la divisa en minúsculas."""
        return self.value.lower()