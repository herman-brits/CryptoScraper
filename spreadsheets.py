#!/usr/bin/evn python3

import gspread
from time import localtime
from time import strftime


class Spreadsheets:
    def __init__(self, bitcoin, ethereum, ripple, bitcoin_cash, litecoin, tether):
        self.crypto_prices = [strftime("%d %B %Y", localtime()), float(bitcoin), float(ethereum), float(ripple), float(bitcoin_cash), float(litecoin), float(tether)]
        print(self.crypto_prices)
        path_to_credentials = ".\\credentials.json"
        key_of_sheet = "XXXXXXXXXXXXXX"
        gc = gspread.service_account(path_to_credentials)
        sh = gc.open_by_key(key=key_of_sheet)
        self.crypto_worksheet = sh.sheet1
        self.upload_row()

    def upload_row(self):
        self.crypto_worksheet.insert_row(self.crypto_prices, 2)