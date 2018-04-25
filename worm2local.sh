#Usage:
#  ./worm2local.sh /worm_backup_2016_07_21_to_2017_01_22/brass/backup/brass/Brass24Tables.09-28-16.tar.Z today_trades.t.bcp.gz 
#
#
#
#
WORM_ARCHIVE=$1
FILE_TO_DOWNLOAD=$2


ssh nitarchive -l brassworm -n "python /users/brassworm/tools/remote_read.py -a $WORM_ARCHIVE -f $FILE_TO_DOWNLOAD; exit;" |gzip -cd>$FILE_TO_DOWNLOAD


exit $!;



