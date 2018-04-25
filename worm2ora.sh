#Usage:
#  ./worm2ora.sh /worm_backup_2016_07_21_to_2017_01_22/brass/backup/brass/Brass24Tables.09-28-16.tar.Z today_trades.t.bcp.gz ctl/rw_trades.ctl
#
#
#
#
WORM_ARCHIVE=$1
FILE_TO_DOWNLOAD=$2
CTL_FILE=$3

rm xaa xab xac xad xae xaf xag xah xai

ssh archive -l test -n "python /users/test/tools/remote_read.py -a $WORM_ARCHIVE -f $FILE_TO_DOWNLOAD; exit;" |gzip -cd|split -l 500000&

for fn in xaa xab xac xad xae xaf xag xah xai; do
	echo $fn
while [ ! -f $fn ]
do
  sleep 1
done
sleep 2
ln -sf $fn $fn.dat
sqlldr userid=stgdata/manage data=$fn.dat control=$CTL_FILE log=sqlloader/$fn.log bad=sqlloader/$fn.bad discard=sqlloader/$fn.dsc parallel=true direct=TRUE&
done


echo 'ssh done'

FAIL=0
for job in `jobs -p`
do
echo $job
    wait $job || let "FAIL+=1"
done
echo $FAIL
if [ "$FAIL" == "0" ];
then
echo "SUCCESS."
else
echo "FAIL! ($FAIL)"
fi

exit $FAIL;



