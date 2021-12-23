#scrapy_absolute_path="$( cd "$( dirname "$0" )" && pwd )/crawler_bmce"
django_absolute_path="$( cd "$( dirname "$0")" && pwd )/risma"
. ~/env/c200_risma/bin/activate
#cd $scrapy_absolute_path && scrapy crawl cours -o ../risma/site_media/bmce/cours/data/bourse.csv -t csv
#cd $django_absolute_path && python manage.py crawler_data_csv bourse_new_data
cd $django_absolute_path && python manage.py  bourse_new_data
python manage.py bourse_new_cours_data
