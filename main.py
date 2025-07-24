import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import csv
from dotenv import load_dotenv
import os

load_dotenv()

# URL para o Webscraping
url = "https://www.mercadolivre.com.br/celular-samsung-galaxy-s24-ultra-256gb-12gb-ram-68-ai-cor-titnio-cinza/p/MLB34491099#polycard_client=search-nordic&searchVariation=MLB34491099&wid=MLB4392480274&position=21&search_layout=stack&type=product&tracking_id=68808753-7f3b-4907-bbe3-6ab1e24efd5c&sid=search"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

# TELEGRAM
token = os.getenv("TOKEN_BOT_TELEGRAM")
chat_id = os.getenv("CHAT_ID_TELEGRAM")
telegram_url = f"https://api.telegram.org/bot{token}/sendMessage"

print("Press Ctrl+C to exit...")

while True:
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")

    price_site = soup.select_one('span.andes-money-amount__fraction').text
    price_str = price_site.strip()
    price_int = int(price_str.replace(".", "").replace(",", ""))

    name_product = soup.select_one("h1.ui-pdp-title").text
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    price_target = 10000

    with open("hist_prices.csv", "a", newline="") as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow([price_int, name_product, date_time, url])

    if price_int <= price_target:
        message = (
            f"⚠️ Oferta encontrada! ⚠️\n\n"
            f"📦 Produto: {name_product}\n\n"
            f"💰 Preço: R$ {price_int}\n\n"
            f"🎯 Alvo: R$ {price_int}\n\n"
            f"⏰ Coletado as: {date_time}\n\n"
            f"🔗 Disponivel em: {url}\n\n"
        )

        requests.post(telegram_url, json={"chat_id": chat_id, "text": message})

    time.sleep(10)