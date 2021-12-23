TODAY=`date +%Y/%m/%d`
LOG_FOLDER="/var/www/vhosts/risma.com/logs/bmce_logs/$TODAY"
NOW=`date +%H%M%S`
LOG_FILE="$LOG_FOLDER/$NOW"
cd /var/www/vhosts/risma.com/c200_risma/
if [ ! -d $LOG_FOLDER ]
then
    mkdir -p $LOG_FOLDER
fi
./bmce_cours.sh > $LOG_FILE
./bmce_indicateur.sh > $LOG_FILE

