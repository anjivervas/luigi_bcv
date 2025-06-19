import requests
from bs4 import BeautifulSoup
from typing import Optional

def get_soup():
    url = "https://bcv.org.ve"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al obtener la página: {e}")
        return None
    
    return BeautifulSoup(response.text, "html.parser")

def get_divisa_div(soup, divisa) -> BeautifulSoup:
    """Extraer el div de la divisa correspondiente"""
    dolar_div=soup.find("div", {"id": f"{divisa}"})
    div_cantidad=dolar_div.find("div", {"class": "col-sm-6 col-xs-6 centrado"}).get_text(strip=True)
    return div_cantidad

def parse_divisa(div_divisa: BeautifulSoup) -> float:
    """Recibe el div de la divisa y devuelve su contenido en formato float"""
    div_parser = div_divisa.strip().replace(",", ".")
    divisa = float(div_parser)
    return divisa

if __name__ == "__main__":
    soup=get_soup()
    divisas=["dolar", "euro", "yuan", "lira", "rublo"]
    for divisa in divisas:
        divisa_div=get_divisa_div(soup, divisa)
        divisa_precio=parse_divisa(divisa_div)
        print(f"Precio del {divisa} para hoy: {divisa_precio}")