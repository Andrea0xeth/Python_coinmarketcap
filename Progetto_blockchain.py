import requests
import time
import schedule
import json
import datetime

class Bot:
    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.params = {
            'start' : '1',
            'limit' : '10',
            'convert': 'EUR'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': "46c8c5a9-b198-4959-87b4-c8df0612fc88",
        }
        self.orders= []

#La criptovaluta con il volume maggiore (in $) delle ultime 24 ore
def fetchCurrenciesData(self):
r = requests.get(url=self.url, headers=self.headers, params=self.params).json()


#Le migliori e peggiori 10 criptovalute (per incremento in percentuale delle ultime 24 ore)
def fetchCurrenciesData(self):



#La quantità di denaro necessaria per acquistare una unità di ciascuna delle prime 20 criptovalute*
def fetchCurrenciesData(self):



#La quantità di denaro necessaria per acquistare una unità di tutte le criptovalute il cui volume delle ultime 24 ore sia superiore a 76.000.000$
def fetchCurrenciesData(self):



#La percentuale di guadagno o perdita che avreste realizzato se aveste comprato una unità di ciascuna delle prime 20 criptovalute* il giorno prima (ipotizzando che la classifca non sia cambiata)
def fetchCurrenciesData(self):



#Per evitare che il vostro programma sovrascriva lo stesso file JSON, denominatelo con la data del momento in cui il programma viene eseguito.


#*Le prime 20 criptovalute secondo la classifica predefinita di CoinMarketCap, quella visibile sul sito, dunque ordinate per capitalizzazione.