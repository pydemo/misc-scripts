#reads data chunk from dev server
#Usage:
#  time ./dev2ora.sh today_trades.t.bcp  1 100
#
#
#
#
#
FILE_TO_DOWNLOAD=$1
#CHUNK_ID=$2
NUM_OF_CHUNKS=$2
CTL_FILE='ctl/rw_trades.ctl'
#pmax=10
fn=$(basename "$FILE_TO_DOWNLOAD")
data=${CHUNK_ID}_${NUM_OF_CHUNKS}_${fn}.bcp


for i in `seq 1 $NUM_OF_CHUNKS`
do
data=${i}_${NUM_OF_CHUNKS}_${fn}.bcp
echo $data
	rm $data
	mkfifo $data
	ssh server -l user -n "python remote_read.py -f  $FILE_TO_DOWNLOAD -i $i -c $NUM_OF_CHUNKS; exit;">$data&
	sleep 0.5
	sqlldr userid=ora/user data=$data control=$CTL_FILE log=sqlloader/$data.log bad=sqlloader/$data.bad discard=sqlloader/$data.dsc parallel=true direct=TRUE&
done
  


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
