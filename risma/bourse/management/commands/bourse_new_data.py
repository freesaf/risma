# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from risma.bourse.models import Indicator
import BeautifulSoup
import requests
import re
class Command(BaseCommand):
    help = """ Extraire des valeurs du site web
    Utilisation : python manage.py webpage_data_scrape"""
    def handle(self, *args, **options):
        url = requests.get('https://www.bmcecapitalbourse.com/bkbbourse/details/1730672%2C102%2C608',verify=False)
        html = BeautifulSoup.BeautifulSoup(url.content)
        price = str(html.find('span', attrs={'class': 'price'}).text).rstrip()
        #Date
        price_float = float(price.replace(',', '.'))
        #Isin
        currency = str(html.find('span', attrs={'class': 'm-detailcurrency'}).text).strip()
        change = str(html.find('span', attrs={'class': re.compile(r'change')}).text)
        #Market center
        change_ = (change.replace(',', '.').replace('%', ''))
        date_time = str(html.find('span', attrs={'class': 'date'}).text.encode('ascii', 'ignore'))
        date = date_time[:10].replace('.', '/')
        time = date_time.rstrip()[-8:-3]
        #Variation
        real_datetime = date + ' ' + time
        header = html.find('div', attrs={'class': 'h1'})
        #Currency
        val1 = str(header.find('span').text.split('(')[1].split(')')[0]).lstrip()
        #Last quote
        val2 = str(header.find('span', attrs={'style': 'font-size:16px'}).text).replace('-', '').strip()
        # curseur
        img_src_value = str(
        html.find('div', attrs={'class': "col-xs-12 col-sm-3 col-md-3 ticker-border"}).find('img')['src'].split(
            '/')[7]).split('.')[0]
        if img_src_value == 'up_data':
            curseur = 'curseurHaut'
        elif img_src_value == 'down_data':
            curseur = 'curseurBas'
        else:
            curseur = 'curseurNulle'
        indicateur = Indicator.objects.create(last_quote= val2, currency= val1,curseur=curseur, variation= real_datetime ,date= price_float, isin= currency,
                                                                        market_center= change_,
                                                                         )
        print("%s  %s  %s  %s   %s  %s") %(price_float, currency, change_, real_datetime, val1,val2)
