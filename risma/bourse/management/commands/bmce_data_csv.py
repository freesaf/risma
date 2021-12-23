#-*- coding: utf-8 -*-
import csv, os
from fnmatch import fnmatch
from django.core.management.base import BaseCommand, CommandError
#from django.contrib.aiuth.models import User
from risma.bourse.models import Cour
from datetime import datetime

class Command(BaseCommand):
    help = """traiter le fichier historique de cours
    Utilisation : python manage.py bmce_data_csv
    """

    def handle(self, *args, **options):
        dossier= "/var/www/vhosts/risma.com/c200_risma/risma/site_media/bmce/indicateur/data"
        #dossier= "/home/apolikamixitos/Documents/bmce/data"
        dossier_dest= "/var/www/vhosts/risma.com/c200_risma/risma/site_media/bmce/indicateur/traite"
        #dossier_dest ="/home/apolikamixitos/Documents/bmce/traitee"
        files = [dossier + os.path.sep + f for f in os.listdir(dossier)]
        for file in files:
            file_name = os.path.basename(file)
            print file_name
            self.read_data(dossier+"/"+file_name)
            os.rename(file, dossier_dest+"/"+file_name)

    def read_data(self, file):
        try:
            x= open(file, 'rb')
            reader = csv.reader(x, delimiter=";")
            #reader = csv.reader(open("/home/apolikamixitos/Documents/bmce/data/histo_1730672_102_608_1400841744613.csv", "r"), delimiter=";")
            print 'file opened and reader ok'
            for i, row in enumerate(reader):
                if not row or i== 0:
                    print 'not row or 0'
                    continue
                else:
                    try:
                      	date, dernier, premier, plus_haut, plus_bas, volume, capitaux= row
                    #except: 
			#print "prob de récup de data sur ligne %s" % i
                        jour= datetime.strptime(date, "%d/%m/%Y")
                        cap = float(capitaux.replace(" ", ""))
                        vol = float(volume.replace(" ", ""))
                        der = float(dernier.replace(" ", ""))
                        pre = float(premier.replace(" ", ""))
                        plh = float(plus_haut.replace(" ", ""))
                        plb = float(plus_bas.replace(" ", ""))
                        try:
                            c, created= Cour.objects.get_or_create(date= jour, dernier =der, premier= pre,
                                                                        plus_haut= plh, plus_bas= plb,
                                                                        volume= vol, capitaux= cap)
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

