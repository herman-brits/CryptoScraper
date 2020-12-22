#!/usr/bin/env python3

import requests
import json


class Scraper:
    def __init__(self, currency):
        self.currency = currency
        self.last = 0
        self.scrape()

    def scrape(self):
        response = requests.get(
            "https://trade.pdax.ph/moon/v1/market/tick/ANX/{currency}PHP".format(currency=self.currency))
        self.response = response
        self.parse()

    def parse(self):
        parseable_response = json.loads(self.response.content)
        self.last = parseable_response['data'][0]['{currency}PHP'.format(currency=self.currency)]['last']
        return float(self.last)
