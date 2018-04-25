#reads data chunk from dev server
#Usage:
#  ./get_chunk_from_dev.sh today_trades.t.bcp  1
#
#
#
#
FILE_TO_DOWNLOAD=$1
CHUNK_ID=$2


fn=$(basename "$FILE_TO_DOWNLOAD")

time ssh test -l user -n "python remote_read.py -f  $FILE_TO_DOWNLOAD -i $CHUNK_ID; exit;">${CHUNK_ID}_${fn}.bcp


exit $!;
