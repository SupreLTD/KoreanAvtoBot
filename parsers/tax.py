import requests


def get_tax(age, engine, power, capacity, price):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'multipart/form-data; boundary=---------------------------94285922528642814993306833942',
        'Origin': 'https://calcus.ru',
        'Connection': 'keep-alive',
        'Referer': 'https://calcus.ru/rastamozhka-auto',
        # 'Cookie': 'PHPSESSID=lnlk36f3k1775k2s3a2c4qan4r',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    data = f'-----------------------------94285922528642814993306833942\r\n' \
           'Content-Disposition: form-data; name="calculate"\r\n\r\n1\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           'Content-Disposition: form-data; name="owner"\r\n\r\n1\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           f'Content-Disposition: form-data; name="age"\r\n\r\n{age}\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           f'Content-Disposition: form-data; name="engine"\r\n\r\n{engine}\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           f'Content-Disposition: form-data; name="power"\r\n\r\n{power}\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           'Content-Disposition: form-data; name="power_unit"\r\n\r\n1\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           f'Content-Disposition: form-data; name="value"\r\n\r\n{capacity}\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           f'Content-Disposition: form-data; name="price"\r\n\r\n{price}\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           'Content-Disposition: form-data; name="currency"\r\n\r\nrub\r\n' \
           '-----------------------------94285922528642814993306833942\r\n' \
           'Content-Disposition: form-data; name="referer"\r\n\r\n' \
           'https%3A%2F%2Fkwork.ru%2F\r\n' \
           '-----------------------------94285922528642814993306833942--\r\n'

    response = requests.post('https://calcus.ru/rastamozhka-auto', headers=headers, data=data)
    return response.json()

