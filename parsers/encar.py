import requests
from bs4 import BeautifulSoup
from datetime import datetime

from parsers.exchange_rates import get_rates


def get_raw_encar(url):
    cookies = {
        '_encar_hostname': 'http://www.encar.com',
        'WMONID': 'ZgsfuLyZLwM',
        'RECENT_CAR_CARID_34333307_1': '34333307%253A%25EB%259E%259C%25EB%2593%259C%25EB%25A1%259C%25EB%25B2%2584%2B%25EB%25A0%2588%25EC%259D%25B8%25EC%25A7%2580%25EB%25A1%259C%25EB%25B2%2584%2BV8%2B5.0%2BSupercharged%25240',
        'RECENT_CAR_CARID_34333407_0': '34333407%253A%25EA%25B8%25B0%25EC%2595%2584%2B%25EC%258F%2598%25EB%25A0%258C%25ED%2586%25A0%2B4%25EC%2584%25B8%25EB%258C%2580%2BHEV%2B1.6%2B4WD%25241',
        'JSESSIONID': 'S0zoeEpACUHqSA6bzOCTyh7RU8stQm21KwDXbxllsn2Pi9w2bFaIBO6rvALpPFC8.mono-was2-prod_servlet_encarWeb5',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        # 'Cookie': '_encar_hostname=http://www.encar.com; WMONID=ZgsfuLyZLwM; RECENT_CAR_CARID_34333307_1=34333307%253A%25EB%259E%259C%25EB%2593%259C%25EB%25A1%259C%25EB%25B2%2584%2B%25EB%25A0%2588%25EC%259D%25B8%25EC%25A7%2580%25EB%25A1%259C%25EB%25B2%2584%2BV8%2B5.0%2BSupercharged%25240; RECENT_CAR_CARID_34333407_0=34333407%253A%25EA%25B8%25B0%25EC%2595%2584%2B%25EC%258F%2598%25EB%25A0%258C%25ED%2586%25A0%2B4%25EC%2584%25B8%25EB%258C%2580%2BHEV%2B1.6%2B4WD%25241; JSESSIONID=S0zoeEpACUHqSA6bzOCTyh7RU8stQm21KwDXbxllsn2Pi9w2bFaIBO6rvALpPFC8.mono-was2-prod_servlet_encarWeb5',
        'Upgrade-Insecure-Requests': '1',
    }

    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.content, 'html.parser')
    year = int(str(soup.find('meta', {'name': 'WT.z_year'})).split()[1].replace('content=', '').replace('"', ''))
    fuel = str(soup.find('meta', {'name': 'whatfuel'})).split()[1].replace('content=', '').replace('"', '')
    price_raw = int(str(soup.find('meta', {'name': 'WT.z_price'})).split()[1].replace('content=', '').replace('"', ''))
    try:
        cap = soup.find('div', {'class': 'prod_infomain'}).find_all('li')[4].text.replace('배기량:', '').replace('c',
                                                                                                              '').replace(
            ',', '')
    except Exception as e:
        cap = soup.find('div', {'class': 'info_product'}).find_all('li')[4].text.replace('배기량:', '').replace('c',
                                                                                                             '').replace(
            ',', '')

    age_raw = datetime.today().year - int(year)

    if age_raw < 3:
        age = '0-3'
    elif 3 <= age_raw <= 5:
        age = '3-5'
    elif 5 < age_raw <= 7:
        age = '5-7'
    else:
        age = '7-0'
    engine = ''
    dvs = 'Не определен'
    if fuel == '가솔린':
        engine = '1'
        dvs = 'Бензин'
    elif fuel == '디젤':
        engine = '2'
        dvs = 'Дизель'
    elif fuel == '가솔린+전기':
        engine = '3'
        dvs = 'Гибрид'

    price = int(((price_raw * 10000) * get_rates()['KRW'][1]) * 1.055)

    return age, engine, cap, price, age_raw, dvs
