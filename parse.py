import requests
from bs4 import BeautifulSoup

def parse():
    URL = 'https://www.banki.ru/products/currency/cash/usd/moskva/'
    HEADER = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/85.0.4183.102 YaBrowser/20.9.2.102 Yowser/2.5 Safari/537.36'
    }
    response = requests.get(URL, headers=HEADER)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('div', class_="table-flex__row text-align-left text-uppercase font-bold font-size-large")
    comps = []

    for item in items:
        comps.append({
            "title": item.find("div", class_="table-flex__cell table-flex__cell--border font-normal color-tealish").get_text(strip=True),
            "CURSE": item.find("div", class_="table-flex__cell table-flex__cell--border").get_text(strip=True),
        })

        for comp in comps:
            print(comp["title"], comp["CURSE"])

parse()
