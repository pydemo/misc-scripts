#!/usr/bin/python 
"""
Usage:
  cd /Bic/scripts/oats/rest/
  python parse_json.py --url --out_file 
  --url 	 : REST endpoint 
  --out_file : output CSV file name	(out.csv)
  
  
  PROD: Move it to /Bic/scripts/mis
  
"""
from __future__ import print_function
import os, time, sys
import urllib2 as urllib
import base64
import json
import logging
import pprint as pp
import atexit
from optparse import OptionParser
from pprint import pprint
import traceback
import hashlib
def formatExceptionInfo(maxTBlevel=5):
	cla, exc, trbk = sys.exc_info()
	excName = cla.__name__
	try:
		excArgs = exc.__dict__["args"]
	except KeyError:
		excArgs = "<no args>"
	excTb = traceback.format_tb(trbk, maxTBlevel)
	#print(excName, excArgs, excTb)
	return ', '.join([excName, excArgs, ', '.join(excTb)])
e=sys.exit
DEFAULT_ENCODING = 'utf-8'
#////////////////////////
EXIT_FAILURE		= 1
EXIT_EMPTY_JSON_DOC= 99
EXIT_BAD_URL		= 100
EXIT_SUCCESS 		= 0
#////////////////////////

#//Python to Oracle column mapping
py2ora=['mgrName',  #MGRNAME
'personalHomePhone',  #PERSONALHOMEPHONE
'division',  #DIVISION
'empGName',  #EMPGNAME
'mgrEmpId',  #MGREMPID
'mcdUserId',  #MCDUSERID
'empMName',  #EMPMNAME
'empLName',  #EMPLNAME
'personalCellPhone',  #PERSONALCELLPHONE
'divisionGroup',  #DIVISIONGROUP
'mgrUserId',  #MGRUSERID
'empId',  #EMPID
'city',  #CITY
'specialtyArea',  #SPECIALTYAREA
'zip',  #ZIP
'title',  #TITLE
'headUserId',  #HEADUSERID
'state',  #STATE
'location',  #LOCATION
'costCenter',  #COSTCENTER
'status',  #STATUS
'empType',  #EMPTYPE
'disabledate',  #DISABLEDATE
'empFName',  #EMPFNAME
'corporateCellPhone',  #CORPORATECELLPHONE
'company',  #COMPANY
'address',  #ADDRESS
'corporat11eWorkPhone',  #CORPORATEWORKPHONE
'termdate',  #TERMDATE
'locationCode',  #LOCATIONCODE
'manager',  #MANAGER
'empName',  #EMPNAME
'country',  #COUNTRY
'region',  #REGION
'costCtrCode',  #COSTCTRCODE
'companyFull',  #COMPANYFULL
'corporateEmail',  #CORPORATEEMAIL
'personalEmail',  #PERSONALEMAIL
'empUserId',  #EMPUSERID
'hiredate',  #HIREDATE
'fullAddr',  #FULLADDR
]
def create_symlink(from_dir, to_dir):
	if (os.name == "posix"):
		os.symlink(from_dir, to_dir)
	elif (os.name == "nt"):
		os.system('mklink /J %s %s' % (to_dir, from_dir))
	else:
		log.error('Cannot create symlink. Unknown OS.', extra=d)
def unlink(dirname):
	if (os.name == "posix"):
		os.unlink(dirname)
	elif (os.name == "nt"):
		os.rmdir( dirname )
	else:
		log.error('Cannot unlink. Unknown OS.', extra=d)
JOB_NAME,_=os.path.splitext(os.path.basename(__file__))
assert JOB_NAME, 'Job name is not set'
#HOME= os.path.dirname(os.path.abspath(__file__))
HOME= r'/Bic/log/mis'
ts=time.strftime('%Y%m%d_%a_%H%M%S')
ts=time.strftime('%Y%m%d_%a')
dr=os.path.dirname(os.path.realpath(__file__))
latest_dir =os.path.join(dr,'log',JOB_NAME,'latest')
ts_dir=os.path.join(dr,'log',JOB_NAME,ts)
config_home = os.path.join(HOME,'config')
latest_out_dir =os.path.join(HOME,'log',JOB_NAME,'output_latest')
ts_out_dir=os.path.join(HOME,'log',JOB_NAME,ts,'output')
latest_dir =os.path.join(HOME,'log',JOB_NAME,'latest')
log_dir = os.path.join(HOME, 'log',JOB_NAME)
ts_dir=os.path.join(log_dir, ts)
header_dir=os.path.join(HOME,'log',JOB_NAME,'headers')
done_file= os.path.join(ts_dir,'DONE.txt')
job_status_file=os.path.join(ts_dir,'%s.%s.status.py' % (os.path.splitext(__file__)[0],JOB_NAME))	
if not os.path.exists(ts_dir):
	os.makedirs(ts_dir)
if not os.path.exists(ts_out_dir):
	os.makedirs(ts_out_dir)

if  os.path.exists(latest_out_dir):
	unlink(latest_out_dir)
#os.symlink(ts_out_dir, latest_out_dir)
create_symlink(ts_out_dir, latest_out_dir)
if  os.path.exists(latest_dir):	
	unlink(latest_dir)
create_symlink(ts_dir, latest_dir)	

DEBUG=0
	
d = {'iteration': 0,'pid':os.getpid(), 'rows':0}
FORMAT = '|%(asctime)-15s|%(pid)-5s|%(iteration)-2s|%(rows)-9s|%(message)-s'
FORMAT = '|%(asctime)-15s%(pid)-5s|%(rows)-9s|%(name)s|%(levelname)s|%(message)s'


log_file_name=os.path.join(ts_dir,'%s_%s.log' % (JOB_NAME,ts))
logging.basicConfig(filename=log_file_name,level=logging.INFO,format=FORMAT)
log = logging.getLogger(JOB_NAME)
log.setLevel(logging.DEBUG)



if not os.path.exists(header_dir):
	os.makedirs(header_dir)
DEFAULT_URL 		= "https://google.com/rest_api"
DEFAULT_OUTPUT_FILE	= os.path.join(latest_dir,'out.csv')
DEFAULT_LOG_TIMESTAMP = ts
DEFAULT_LOG_RETENTION_DAYS	= 3
DEFAULT_HEADER ='mgrName,personalHomePhone,division,empGName,mgrEmpId,mcdUserId,empMName,empLName,personalCellPhone,divisionGroup,mgrUserId,empId,city,specialtyArea,zip,title,headUserId,state,location,costCenter,status,empType,disabledate,empFName,corporateCellPhone,company,address,corporateWorkPhone,termdate,locationCode,manager,empName,country,region,costCtrCode,companyFull,corporateEmail,personalEmail,empUserId,hiredate,fullAddr' +os.linesep
exit_status={}
exit_status['Exception']=None

def save_status():
	global job_status_file, exit_status,header_file_name, opt, d
	if 1:
		p = pp.PrettyPrinter(indent=4)
		with open(job_status_file, "w") as py_file:			
			py_file.write('status=%s' % (p.pformat(exit_status)))
			#log.info (job_status_file, extra=d)
	#create out file with error message
	if not os.path.isfile(opt.out_file):
		if  os.path.isfile(header_file_name):
			log.info('Using header file.', extra=d)
			with open(header_file_name, "rb") as fheader:
				header = fheader.read()
		else:
			header=DEFAULT_HEADER
			log.warn('Using default HEADER because header file does not exists.', extra=d)
		with open(opt.out_file, "wb") as fh:
			if header:
				fh.write(header)
				err='"ERROR. Check log file."'
				#print (exit_status['Exception'])
				if exit_status['Exception']:
					print (exit_status['Exception'])
					#e(0)
					err='"%s"' % exit_status['Exception'][:50].replace(os.linesep, ' ')
				fh.write(err+(len(header.split(opt.col_delim))-1)*opt.col_delim + os.linesep)
				log.info('Output file with error: \n' +opt.out_file, extra=d)
	else:
		pass
DEFAULT_NULL_VALUE	=	'null'
boo={'TRUE':'1', 'FALSE':'0'}
import types
def process_value(col_id, key,value,encoding, col_mask):
	if col_mask[col_id]: # check if column exists in predefined col list
		if value: 
			#pprint(dir(types))
			if type(value) is unicode:
				#print(type(value))
				#print (1)
				try:
					val=value.encode(encoding)
					return val
				except err:
					log.warn('Could not encode value for key "%s".' % str(key), extra=d)
					try:
						last_chance_val= str(value)
						return last_chance_val
					except last_err:
						exit_status['Error']=formatExceptionInfo()
						log.error('Could not convert value for key "%s".' % str(key), extra=d)
						log.error(formatExceptionInfo, extra=d)
						raise
			elif type(value) is bool:
				return boo[str(value).strip().upper()]
			else:
				return str(value).strip()
		else:
			return DEFAULT_NULL_VALUE
	else:
		return DEFAULT_NULL_VALUE
if __name__ == "__main__":	
	atexit.register(save_status)
	parser = OptionParser()
	parser.add_option("-u", "--url", dest="url", type=str, default=DEFAULT_URL)
	parser.add_option("-c", "--col_delim", dest="col_delim", type=str, default=',')
	parser.add_option("-U", "--user_name", dest="user_name", type=str, default='srvc_wday_dwh')
	parser.add_option("-P", "--user_pwd", dest="user_pwd", type=str, default='')
	parser.add_option("-e", "--add_header",  action="store_true", dest="add_header", default=True,
                  help="Add header record to output CSV file.")
	parser.add_option("-d", "--delete_existing_out_file",  action="store_true", dest="delete_existing_out_file", default=True,
                  help="Delete existing out file before parse.")
	parser.add_option("-o", "--out_file", dest="out_file", type=str, default=DEFAULT_OUTPUT_FILE)
	parser.add_option("-j", "--job_name", dest="job_name", type=str, default=JOB_NAME)
	parser.add_option("-t", "--log_timestamp", dest="log_timestamp", type=str, default=DEFAULT_LOG_TIMESTAMP)
	parser.add_option("-r", "--log_retention_days", dest="log_retention_days", type=str, default=DEFAULT_LOG_RETENTION_DAYS)
	parser.add_option("-L", "--hide_log_output",  action="store_true", dest="hide_log_output", default=False, help="Suppress terminal log messages.")
	
	(opt, args) = parser.parse_args()
	if not opt.hide_log_output:
		ch = logging.StreamHandler(sys.stdout)
		ch.setLevel(logging.DEBUG)
		formatter = logging.Formatter(FORMAT)
		ch.setFormatter(formatter)
		log.addHandler(ch)
	log.info('Log file:\n%s' % log_file_name, extra=d)
	#print (opt.url)
	header_file_base=hashlib.sha224(opt.url).hexdigest()+'.csv'
	header_file_name= os.path.join(header_dir,header_file_base)
	
	if opt.delete_existing_out_file and os.path.isfile(opt.out_file):
		os.remove(opt.out_file)
		log.info('Existing file removed.', extra=d)	
	#e(0)
	#log cleanup
	if float(opt.log_retention_days):
		
		cmd ='find {log_dir}/* -type d -ctime {log_retention_days} | xargs rm -rf'.format(log_dir=log_dir,log_retention_days=opt.log_retention_days)
		exit_status['delete_log_retention'] = cmd
		status=os.system(cmd)
		assert not status, 'Log deletion failed with status {status}.'.format(status=status)
	urlResponse=None
	
	#pprint(dir(urllib))
	try:
		request = urllib.Request(opt.url)
		base64string = base64.b64encode('%s:%s' % (opt.user_name, opt.user_pwd))
		request.add_header("Authorization", "Basic %s" % base64string)   
		urlResponse = urllib.urlopen(request)
		#urlResponse  = urllib.urlopen(opt.url)
	except urllib.HTTPError, e:
		exit_status['Exception']=str(e.code)	
		#log.error('HTTPError = ' + str(e.code), extra=d)	
		#raise e
	except urllib.URLError, e:
		exit_status['Exception']=str(e.code)	
		#log.error('URLError = ' + str(e.reason), extra=d)
		#raise e
	#except urllib.HTTPException, e:
	#	exit_status['Exception']=str(e.reason)	
	#	log.error('HTTPException', extra=d)
	#	#raise e
	except Exception as e:
		exit_status['Exception']=formatExceptionInfo()	
		#log.error(formatExceptionInfo(), extra=d)
		#raise e
	if urlResponse:		
		if hasattr(urlResponse.headers, 'get_content_charset'):
			encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
		else:
			encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
		#print (encoding)
		#e(0)

		data = json.loads(urlResponse.read())
		meta=data[u'response'][u'metadata']
		results=data[u'response'][u'searchResults']
		#print (results)
		#e(0)
		header=None
		col_mask=None 
		
		#e(0)
		if opt.add_header:
			header=opt.col_delim.join(results[0].keys())
			hl= str(header).split(',')
			col_mask=[True]* len(hl)
			if 0:
				for i, col in enumerate(hl):
					if str(col).strip().upper() not in [str(c).strip().upper() for c in py2ora]:
						col_mask[i] = False
						log.warn('Column "%s" does not exists in predefined col list. Passing...' % str(col), extra=d )
				#pprint(col_mask)
			
			#e(0)
		if data:
		
			with open(opt.out_file, "wb") as fh:
				if header:
					fh.write(header+os.linesep)
					if not os.path.isfile(header_file_name):
						log.info('Creating header file.', extra=d)
						with open(header_file_name, "wb") as fheader:
							fheader.write(header+os.linesep)
				for row in results:
					#pprint(row)
					#e(0)
					try:
						l=('"%s"' % opt.col_delim).join([process_value(id, key,row[key], encoding,col_mask) for id,key in enumerate(row.keys())])+'"'
						#print(l)
						#e(0)
					except Exception, err:
						#pprint(row)
						#for r, v in row.items():
						#	print (r, v)
							#print (r.encode(encoding) )
						log.error(formatExceptionInfo())
						raise
					fh.write(('"'+l).replace('"%s"' % DEFAULT_NULL_VALUE,'')+os.linesep)
					#print (('"'+l).replace('"%s"' % DEFAULT_NULL_VALUE,'')+os.linesep)
					#pprint(l.replace('"null"',''))
					#print (l.replace('"%s"' % DEFAULT_NULL_VALUE,''))
					#e(0)

			assert meta[u'resultSet'][u'count'] in [len(results)], 'Row count mismatch JSON vs CSV (%s/%s)' % (meta[u'resultSet'][u'count'] , [len(results)])
			d['rows']=meta[u'resultSet'][u'count']
			log.info('Counts ok', extra=d)
			log.info('Output file: \n' +opt.out_file, extra=d)
		else:
			if  os.path.isfile(header_file_name):
				log.info('Using header file.', extra=d)
				with open(header_file_name, "rb") as fheader:
					header = fheader.read()
			else:
				header=DEFAULT_HEADER
				log.warn('Using default HEADER because header file does not exists.', extra=d)
			with open(opt.out_file, "wb") as fh:
				if header:
					fh.write(header)
					err='"ERROR: JSON document is empty."'
					if exit_status['Exception']:
						err=exit_status['Exception'].replace(os.linesep,' ')[:50]
					fh.write(err+(len(header.split(opt.col_delim))-1)*opt.col_delim + os.linesep)
					log.info('Output file with error: \n' +opt.out_file, extra=d)

			exit_status['Error']='JSON document is empty.'	
			log.error('JSON document is empty.', extra=d)
			e(EXIT_EMPTY_JSON_DOC)

	else:
		
		log.error('Bad URL.', extra=d)
		#if exit_status['Exception']:
		#	log.error(exit_status['Exception'], extra=d)

		exit(EXIT_BAD_URL)
	if not exit_status['Exception']:
		exit(EXIT_SUCCESS)
	else:
		exit(EXIT_FAILURE)

