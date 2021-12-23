#-*- coding: utf-8 -*-
import csv, os
from fnmatch import fnmatch
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from risma.bourse.models import Indicator
from datetime import datetime

class Command(BaseCommand):
    help = """traiter le fichier historique de cours
    Utilisation : python manage.py crawler_data_csv
    """

    def handle(self, *args, **options):
        #dossier= "/home/apolikamixitos/Documents/bmce/data"
        #dossier_dest ="/home/apolikamixitos/Documents/bmce/traitee"
        dossier= "/var/www/vhosts/risma.com/c200_risma/risma/site_media/bmce/cours/data"
        dossier_dest= "/var/www/vhosts/risma.com/c200_risma/risma/site_media/bmce/cours/traite"
        files = [dossier + os.path.sep + f for f in os.listdir(dossier)]
        for file in files:
            file_name = os.path.basename(file)
            print file_name
            self.read_data(dossier+"/"+file_name)
            os.rename(file, dossier_dest+"/"+file_name)

    def read_data(self, file):
        #file = "/home/apolikamixitos/Documents/bourse.csv"
        try:
            x= open(file, 'rb')
            reader = csv.reader(open(file, "r"), delimiter=",")
            for i, row in enumerate(reader):
                if not row or i== 0:
                    print 'not row or 0'
                    continue
                else:
                    try:
                        curseur, currency, market_center, date, isin, variation, last_quote = row
                        print row
                        try:
                            c, created= Indicator.objects.get_or_create(last_quote= last_quote, currency= currency, variation= variation,
                                                                         curseur =curseur, date= date, isin= isin,
                                                                        market_center= market_center,
                                                                         )
                        except:
                            print "erreur de creation de  lobject pour la ligne %s" % i
                            continue

                        if created:
                            c.save()
                            print "created : %s " % i

                    except:
                        print "probleme de récupération de data sur la ligne %s" % i
                        continue
        except:
            print "Fichier pas ouvert : %s" % (file)
            return
          
