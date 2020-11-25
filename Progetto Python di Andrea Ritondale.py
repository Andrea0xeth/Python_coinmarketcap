import requests
import time
import schedule
import json
import datetime
from datetime import datetime

dyesterday = None


def __init__(fetchedCurrenciesData):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    params = {'start': '1',
              'limit': '100',
              'convert': 'USD'}

    headers = {'Accepts': 'application/json',
               'X-CMC_PRO_API_KEY': '46c8c5a9-b198-4959-87b4-c8df0612fc88'}

    r = requests.get(url=url, headers=headers, params=params).json()
    d = {}
    for currency in r['data']:
        d[currency['name']] = currency['quote']['USD'][fetchedCurrenciesData]
    return d


def analysis(bestV=1, highest_p=10, lowest_p=10, unit_usd_capitalization=20, usd_highet_volume=76000000, gain_loss=20):

    d1 = __init__(fetchedCurrenciesData='volume_24h')
    sort_d1 = {k: v for k, v in sorted(d1.items(), key=lambda x: x[1], reverse=True)}
    bestV_highest = dict(list(sort_d1.items())[0:bestV])

    d2 = __init__(fetchedCurrenciesData='percent_change_24h')
    sort_d2 = {k: v for k, v in sorted(d2.items(), key=lambda x: x[1], reverse=True)}
    sort_d2_highest = dict(list(sort_d2.items())[0:highest_p])
    sort_d2_lowest = dict(list(sort_d2.items())[:-lowest_p - 1:-1])

    d3 = __init__(fetchedCurrenciesData='price')
    d3_first_unit_usd_capitalization = dict(sorted(list(d3.items())[0:unit_usd_capitalization], key=lambda x: x[1], reverse=True))
    d3_first_unit_usd_capitalization['TOTAL_PRICE'] = round(sum(d3.values()), 2)

    d4 = {}
    d4_step1 = d1  
    d4_step2 = d3  
    for (k, v), (k2, v2) in zip(d4_step1.items(), d4_step2.items()):
        if v > usd_highet_volume:
            d4[k] = v2
    d4 = dict(sorted(list(d4.items()), key=lambda x: x[1], reverse=True))
    d4['TOTAL_PRICE'] = round(sum(d4.values()), 2)

    
    price = __init__(fetchedCurrenciesData='price')
    price_first_gain_loss = dict(sorted(list(price.items())[0:gain_loss], key=lambda x: x[1], reverse=True))
    percent_change = __init__(fetchedCurrenciesData='percent_change_24h')
    percent_change_first_gain_loss = dict(sorted(list(percent_change.items())[0:gain_loss], key=lambda x: x[1], reverse=True))
    price_yesterday_first_gain_loss = {}
    for k, v in price_first_gain_loss.items():
        for k2, v2 in percent_change_first_gain_loss.items():
            if k == k2:
                price_yesterday_first_gain_loss[k] = v - ((v2 / 100) * v)
    total_price_today = round(sum(price_first_gain_loss.values()), 4)
    total_price_yesterday = round(sum(price_yesterday_first_gain_loss.values()), 4)
    d5 = percent_change_first_gain_loss
    d5['TOTAL_GAIN/LOSS_PERCENTAGE'] = ((total_price_today - total_price_yesterday)/total_price_today)*100

    results = {"The Crypto with the best volume in 24H is ": bestV_highest,

             "The ten cryptocurrencies with the highest percent increase in 24H are ": sort_d2_highest,
             "The ten cryptocurrencies with the lowest percent increase in 24H are ": sort_d2_lowest,
             "The USD needed to buy one unit of these first " + str(unit_usd_capitalization) + " cryptocurrencies by market capitalization is": d3_first_unit_usd_capitalization,
             "The total price in US Dollars necessary to buy one unit of all these " + str(len(d4) - 1) + " cryptocurrencies whose volume is higher than " + str(usd_highet_volume) + " is": d4,

             "The percentage of gain or loss maded if you had bought one unit of each " + str(gain_loss) + " top cryptocurrencies in marketcap order on the previous day is ": d5
             }

    with open("analysis_of_"+""+datetime.now().strftime("%Y_%m_%d-%I.%M.%S_%p")+".json", "w") as outfile:
        json.dump(results, outfile, indent=4)

schedule.every().day.at("19:59:10").do(analysis, bestV=1, highest_p=10, lowest_p=10, unit_usd_capitalization=20, usd_highet_volume=76000000, gain_loss=20)


while True:
    schedule.run_pending()
    time.sleep(1)
