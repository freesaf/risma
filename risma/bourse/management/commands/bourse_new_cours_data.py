# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from risma.bourse.models import Cour
from datetime import datetime
import BeautifulSoup
import requests
class Command(BaseCommand):
    help = """ Extraire des valeurs du site web
    Utilisation : python manage.py gat_cour_data"""
    def handle(self, *args, **options):
        url = requests.get('https://www.bmcecapitalbourse.com/bkbbourse/details/hiku/1730672,102,608',verify=False)
        html = BeautifulSoup.BeautifulSoup(url.content)
        div = html.find('div', attrs={'class': 'hikuResult'})
        tr = div.findAll('tr')[1:]
        for t in tr[::-1]:
            datefield, premier, dernier, high, low, volume, capitaux = self.get_val(t)
            try:
                cour, created = Cour.objects.get_or_create(
                    date=datefield,
                    premier=premier,
                    dernier=dernier,
                    plus_haut=high,
                    plus_bas=low,
                    volume=volume,
                    capitaux=capitaux)
                print self.get_val(t)
                if not created:
                    print("not createddddddddddddddddddddddd")
            except:
                pass
    def get_val(self,t):
        date_time = t.find('td', attrs={"class": "datetime l"}).text.encode('ascii', 'ignore')

        datefield = datetime.strptime(date_time, "%d.%m.%Y").date()
        try:
            premier = float(t.find('td', attrs={"class": "open r"}).text.encode('ascii', 'ignore').replace(',', "."))
        except:
            premier = None
        try:
            dernier = float(t.find('td', attrs={"class": "last r"}).text.encode('ascii', 'ignore').replace(',', "."))
        except:
            dernier = None
        try:
            high = float(t.find('td', attrs={"class": "high r"}).text.encode('ascii', 'ignore').replace(',', "."))
        except:
            high = None
        try:
            low = float(t.find('td', attrs={"class": "low r"}).text.encode('ascii', 'ignore').replace(',', "."))
        except:
            low = None
        try:
            volume = float(t.findAll('td', attrs={"class": "volume r"})[0].text.encode('ascii', 'ignore'))
        except:
            volume = None
        try:
            capitaux = float(t.findAll('td', attrs={"class": "volume r"})[1].text.encode('ascii', 'ignore'))
        except:
            capitaux = None
        return datefield,premier, dernier, high, low, volume, capitaux
