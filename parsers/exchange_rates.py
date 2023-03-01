import datetime
from pycbrf import ExchangeRates


def get_rates():
    rates = {}
    to_show_rates = ['USD', 'KRW','RUB']
    today = str(datetime.datetime.now())[:10]
    rates_today = ExchangeRates(today)
    for rate in list(filter(lambda el: el.code in to_show_rates, rates_today.rates)):
        rates[rate.code] = [rate.name, float(rate.rate), float(rate.value)]
    return rates




