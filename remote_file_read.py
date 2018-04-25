#!/usr/bin/python
import socket 
import sys, time, os
import datetime as dt
from optparse import OptionParser
import tempfile
import errno
from subprocess import Popen, PIPE

e=sys.exit

home= os.path.dirname(os.path.abspath(__file__))

SUCCESS = 0 
DEBUG  = 0
DEFAULT_CHUNK_BYTES = 1024*1024*10	
def get_dump_file_name(fn):
	global home
	tmp_dir= os.path.join(home,opt.tar_name.strip('/'))
	if not os.path.isdir(tmp_dir):
		os.makedirs(tmp_dir)
	return (tmp_dir,os.path.join(tmp_dir,fn))
	
def Monitor(path):	
	global opt
	#create tmp dir

	dirn,fn=get_dump_file_name(opt.file_to_extract_from_tar)
	#print fn
	#e(0)
	archive= opt.tar_name 
	os.chdir(dirn)
	cmd='time tar --extract  --file=%s %s; exit;' % (archive, opt.file_to_extract_from_tar)  #.split(' ')
	#print cmd
	p = Popen(cmd, stdout=PIPE, stderr=PIPE,shell=True)
	while not os.path.isfile (fn):
	
		if DEBUG:
			print('waiting for file.')
		time.sleep(1)
	fh=open(fn,'rb')
	i=0
	chunk=opt.chunk_size_bytes
	while p.poll() is None:
		if DEBUG:
			l= len(fh.read())
			print i,l
		else:
			sys.stdout.write( fh.read(chunk))
		i +=1
		#time.sleep(0.01)
	
	#output, err = p.communicate()
	#print output, err 
	status= p.wait()
	if DEBUG:
		print 'last', len(fh.read())
	else:
		sys.stdout.write(  fh.read())
	fh.close()
	return status
	
def Send_File(path):	
	global opt
	status=0
	fn=opt.file_to_extract_from_tar
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
	parser.add_option("-f", "--file_to_extract_from_tar", dest="file_to_extract_from_tar", type=str, default='today_trades.t.bcp.gz')
	
	parser.add_option("-a", "--tar_name", dest="tar_name", type=str, default='/worm_backup_2016_07_21_to_2017_01_22/brass/backup/brass/Brass24Tables.09-28-16.tar.Z')
	parser.add_option("-c", "--chunk_size_bytes", dest="chunk_size_bytes", type=str, default=DEFAULT_CHUNK_BYTES)
	parser.add_option("-d", "--delete_existing_file",  action="store_true", dest="delete_existing_file", default=False, help="Delete existing file before extract.")
	(opt, args) = parser.parse_args()
	dirn,fn=get_dump_file_name(opt.file_to_extract_from_tar)
	if opt.delete_existing_file:
		
		if os.path.isfile(fn):
			try:
				os.unlink(fn)
			except  e:
				print str(e)
				raise
		Monitor(opt.file_to_extract_from_tar)
	else: #file exists. just send it over
		Send_File(fn)
		
	e(SUCCESS)

