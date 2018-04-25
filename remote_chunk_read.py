#!/usr/bin/python
#Usage:
#   Execute if from prod like this:
#   ssh nitarchive -l brassworm -n "python /Bic/scripts/oats/tools/remote_read/remote_read.py -f $FILE_TO_DOWNLOAD; exit;"
#
import socket 
import sys, time, os
import datetime as dt
from optparse import OptionParser
import tempfile
import errno
from subprocess import Popen, PIPE
from pprint import pprint

e=sys.exit

home= os.path.dirname(os.path.abspath(__file__))

SUCCESS = 0 
DEBUG  = 0
DEFAULT_CHUNK_BYTES = 1024*1024*10	

chunks=[(0,1024*1024*10),]
readsize=1024*64	
def Send_Chunk(path, cut):	
	global opt
	fromb,bytes_to_read=cut
	read_so_far=0
	status=0
	fn=opt.file_to_send
	fh=open(fn,'rb')
	i=0
	fh.seek(fromb)
	if bytes_to_read<readsize:
		chunk=fh.read(bytes_to_read)
		sys.stdout.write(chunk)
		return status
	else:
		chunk=fh.read(readsize)
		sys.stdout.write(chunk)
		read_so_far +=readsize

	while chunk:
		if read_so_far+readsize>bytes_to_read:
			chunk=fh.read(bytes_to_read-read_so_far)
			sys.stdout.write(chunk)
			break
		else:
			chunk=fh.read(readsize)
			sys.stdout.write(chunk)
			read_so_far +=readsize
	fh.close()
	return status
	
def Send_File(path):	
	global opt
	status=0
	fn=opt.file_to_send
	fh=open(fn,'rb')
	i=0
	chunk_size=opt.chunk_size_bytes
	chunk=fh.read(chunk_size)
	sys.stdout.write(chunk)

	while chunk:
		chunk=fh.read(chunk_size)
		sys.stdout.write(chunk)
	fh.close()
	return status


if __name__ == '__main__':

	
	parser = OptionParser()	
	parser.add_option("-f", "--file_to_send", dest="file_to_send", type=str, default='today_trades.t.bcp')
	
	#parser.add_option("-a", "--tar_name", dest="tar_name", type=str, default='/worm_backup_2016_07_21_to_2017_01_22/brass/backup/brass/Brass24Tables.09-28-16.tar.Z')
	parser.add_option("-c", "--num_of_chunks", dest="num_of_chunks", type=int, default=10)
	parser.add_option("-i", "--chunk_id", dest="chunk_id", type=int, default=0)
	#parser.add_option("-d", "--delete_existing_file",  action="store_true", dest="delete_existing_file", default=False, help="Delete existing file before extract.")
	(opt, args) = parser.parse_args()
	if opt.chunk_id:
		fn=opt.file_to_send
		cuts=[]
		statinfo = os.stat(fn)
		fsize= statinfo.st_size

		chunk=int(fsize/opt.num_of_chunks)
	
		with open(fn, 'rb') as fh:
			
			curpos=0
			new_chunk_size=chunk
			for i in range(opt.num_of_chunks):
				fh.seek(chunk, os.SEEK_CUR)
				
				pos = fh.tell()
				l=fh.readline()
				partial_line=fh.tell()-pos
				new_chunk_size=fh.tell() - pos
				#print new_chunk_size
				cuts.append([curpos,fh.tell()-curpos])
				curpos=fh.tell()
		#pprint(cuts)
		#e(0)
		Send_Chunk(opt.file_to_send, cuts[opt.chunk_id-1])
	else: # send the whole file
		Send_File(opt.file_to_send)
		
	e(SUCCESS)


	
	
