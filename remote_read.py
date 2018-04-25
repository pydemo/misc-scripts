#!/usr/bin/python
import socket 
import sys, time, os
import datetime as dt
from optparse import OptionParser
import tempfile
import errno
from subprocess import Popen, PIPE
e=sys.exit

def tail( f, lines=20 ):
	total_lines_wanted = lines

	BLOCK_SIZE = 1024
	f.seek(0, 2)
	block_end_byte = f.tell()
	lines_to_go = total_lines_wanted
	block_number = -1
	blocks = [] # blocks of size BLOCK_SIZE, in reverse order starting
				# from the end of the file
	while lines_to_go > 0 and block_end_byte > 0:
		if (block_end_byte - BLOCK_SIZE > 0):
			# read the last block we haven't yet read
			f.seek(block_number*BLOCK_SIZE, 2)
			blocks.append(f.read(BLOCK_SIZE)) 
		else:
			# file too small, start from begining
			f.seek(0,0)
			# only read what was not read
			blocks.append(f.read(block_end_byte))
		lines_found = blocks[-1].count('\n')
		lines_to_go -= lines_found
		block_end_byte -= BLOCK_SIZE
		block_number -= 1
	all_read_text = ''.join(reversed(blocks))
	return '\n'.join(all_read_text.splitlines()[-total_lines_wanted:])
import stat
def isWritable_2(name):
	uid = os.geteuid()
	gid = os.getegid()
	s = os.stat(name)
	mode = s[stat.ST_MODE]
	print stat.ST_MODE
	return (
		((s[stat.ST_UID] == uid) and (mode & stat.S_IWUSR)) or
		((s[stat.ST_GID] == gid) and (mode & stat.S_IWGRP)) or
		(mode & stat.S_IWOTH)
		)

import fcntl

def acquireLock(path):
	''' acquire exclusive lock file access '''
	locked_file_descriptor = open(path, 'w+')
	fcntl.lockf(locked_file_descriptor, fcntl.LOCK_EX)
	return locked_file_descriptor

def releaseLock(locked_file_descriptor):
	''' release exclusive lock file access '''
	locked_file_descriptor.close()

		
def isWritable(path):
    try:
        testfile = tempfile.TemporaryFile(path)
        testfile.close()
    except OSError, e:
        if e.errno == errno.EACCES:  # 13
            return False
        e.filename = path
        raise
    return True

DEBUG=0
def Monitor(path):
	#os.chdir('/Bic/scripts/oats/fix/missing_oats/SAMM_file_reload')
	global opt
	fn=opt.file_to_extract_from_tar
	archive= opt.tar_name 
	#home= os.path.dirname(os.path.abspath(__file__))
	#path_to_archive = os.path.join(home,archive)
	cmd='time tar --extract  --file=%s %s' % (archive, fn)  #.split(' ')
	p = Popen(cmd, stdout=PIPE, stderr=PIPE,shell=True)
	while not os.path.isfile (fn):
		if DEBUG:
			print('waiting for file.')
		time.sleep(1)
	fh=open(fn,'rb')
	i=0
	chunk=1024*1024*10
	prev_len=-1
	while p.poll() is None:
		#print('Reading file.')
		#print(fh.read(1024*1024))
		if DEBUG:
			l= len(fh.read())
			print i,l
			if l==prev_len and l==0:
				e(0)
			prev_len=l
		else:
			sys.stdout.write( fh.read(chunk))
		#if not l:
		#	e(0)
		i +=1
		#time.sleep(0.01)
	
	output, err = p.communicate()
	#print output, err 
	status= p.wait()
	if DEBUG:
		print 'last', len(fh.read())
	else:
		sys.stdout.write(  fh.read())
	fh.close()
	return status
	
	

		

#from filelock import FileLock
		
def print_error():
	exc, err, traceback = sys.exc_info()
	print ('Connection to ')
	print (exc, traceback.tb_frame.f_code.co_filename, 'ERROR ON LINE', traceback.tb_lineno, '\n', err)
	del exc, err, traceback	
DEFAULT_CHUNK_BYTES = 10000	


if __name__ == '__main__':

	
	parser = OptionParser()
	#parser.add_option("-i", "--input_file", dest="input_file", type=str, default='/Bic/scripts/oats/py27/bin/log/testjob/2017-02-08-101243/testjob_2017-02-08-101243.log')
	parser.add_option("-f", "--file_to_extract_from_tar", dest="file_to_extract_from_tar", type=str, default='today_trades.t.bcp.gz')
	parser.add_option("-a", "--tar_name", dest="tar_name", type=str, default='/worm_backup_2016_07_21_to_2017_01_22/brass/backup/brass/Brass24Tables.09-28-16.tar.Z')
	parser.add_option("-c", "--chunk_size_bytes", dest="chunk_size_bytes", type=str, default=DEFAULT_CHUNK_BYTES)
	(opt, args) = parser.parse_args()
	Monitor(opt.file_to_extract_from_tar)
	e(0)

