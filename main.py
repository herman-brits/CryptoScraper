#!/usr/bin/env python3

import requests
import json
import gspread
from datetime import date
from scraper import Scraper
from spreadsheets import Spreadsheets

def main():
    bitcoin_price = Scraper(currency="BTC")
    ethereum_price = Scraper(currency="ETH")
    ripple_price = Scraper(currency="XRP")
    bitcoin_cash_price = Scraper(currency="BCH")
    litecoin_price = Scraper(currency="LTC")
    tether_price = Scraper(currency="USDT")
    Spreadsheets(bitcoin=bitcoin_price.parse(), ethereum=ethereum_price.parse(), ripple=ripple_price.parse(), bitcoin_cash=bitcoin_cash_price.parse(),
                 litecoin=litecoin_price.parse(), tether=tether_price.parse())

main()