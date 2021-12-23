scrapy_absolute_path="$( cd "$( dirname "$0" )" && pwd )/crawler_bmce"
django_absolute_path="$( cd "$( dirname "$0")" && pwd )/risma"
. ~/env/c200_risma/bin/activate
cd $scrapy_absolute_path && scrapy crawl indicateur
cd $django_absolute_path && python manage.py bmce_data_csv

