from app.core import BCVScraper, Divisas

scraper = BCVScraper()
precios = scraper.obtener_tasa(Divisas.DOLAR)   

lista_divisas = Divisas.to_list()
for divisa in lista_divisas:
    precio = scraper.obtener_tasa(divisa)
    print(f"El precio de {divisa.value} es: {precio}")