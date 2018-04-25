import sys, re
sys.path.append("./mechanize")
e=sys.exit
from mechanize import Browser
import time, random






#modify
#page = br.open("http://www.dice.com/profman/servlet/ProfMan?op=1011&MENU_PROFILES=04064328d2cb304244e7a91114f47d3c&MENU_EDIT=Edit")
def update_resume(dockey):
	#Edit
	response = br.open("https://secure.dice.com/regman/profile.html?dockey=%s" % dockey)
	#					 https://secure.dice.com/regman/profile.html?dockey=512eb2546eaa3d334b77c4de2fc5156a
	#response = br.open("http://www.dice.com/profman/servlet/ProfMan?op=1040")
	#print page.read()
	#for f  in br.forms():
	#	print f.name
	
	rp_data = response.get_data()
	#print rp_data	
	rp_data = re.sub(r'<optgroup label=".+"/>', "", rp_data)
	rp_data = re.sub(r'</optgroup>', "", rp_data) # replace all optgroup elements
	response.set_data(rp_data)
	#print response.read()
	#sys.exit(1)
	br.set_response(response)	
	#sys.exit(1)
	br.select_form(name="profileSection2")
	#send login information
	ct=time.ctime()
	cv= """/* %s */

|-----------------|
|  $100/hour C2C  |				
|-----------------|

Self-incorporated (sCorp).


ALEX BUZUNOV 

 Mobile: (646) 801-8671
 Location: Jersey City, NJ

 SKILLS: Databases: Oracle 7.3.3 8i 9i 10G 11G R2, Sybase System 10, KDB+; 
 Languages: PL SQL, Python Perl PHP, Q, and SQL; 
 NoSQL: Bigtable, Netezza HBase Nive; 
 BI Appliance: Exadata V2, Netezza, Vertica, ParAccel; 
 ER Tools: PowerDesigner and Erwin; SAM: Rational ClearCase, CVS, Perforce; 
 Tools: gdb, ant, Autosys, ADDM, AWR, bash, exp, imp, JIRA, SQL*Loader, SQL*Plus, SQL*Trace, Toad, tkprof, and XMLSpy; 
 Google: Borg, GFS, Mapreduce, Sawzall, Bigtable; 
 Netezza: Aginity Workbench, NZPLSQL, UDF UDX;


 EXPERIENCE:
 CONFIDENTIAL, JERSEY CITY, NJ (Aug. 09 Present) 
 SR ORACLE DEVELOPER (Consultant) 
 As Global US Markets Analytic Technology team member I'm mostly involved in Data Warehousing and ETL development and BI Appliance evaluation.
 Using Python, SQL*Plus, and SQL*Loader created set of scripts for ad-hoc data replication from/to upstream and downstream environments. Functionality including file-to-db, db-to-db, db-to-file. Supports table data sharding, partitioning, index rebuild, column splicing. Touch and go design allows you to specify table name or SQL and it will proceed with parallel direct data load using SQL*Loader. Used for multi-terabyte data load/transfer on daily basis. ~2500partitions/ 70mil rec/partition/250 columns.
 Using PL/SQL created package for partitioned and sub-partitioned table compression. 
 Designed and implemented pseudo multi-processing in PL/SQL using DBMS_SQL. Implemented wait (join) functionality. User would create SQL/DML/DDL payload, append to queue and run etl pipeline.
 Using wxPython created front-end for ad-hoc data management scripts.
 Worked with architects, DBAs, business analysts to understand overall integration direction.
 Reviewed testing approach used by the team. Ensured best coding practices.
 Pro-actively identified and resolved potential problems. 
 Actively contributed to other applications development. Provided guidance to other developers.
 Participated in technical design reviews, functional spec reviews, project estimates, code reviews.
 Tuned SQL ad-hock queries and PL SQL code.
 Created PL SQL package for ad-hoc partition compression.
 In scope of BI Appliance evaluation scripted TradeVolumes code and data migration from Oracle 10G to Exadata, Paraccel, Netezza, and Hadoop HBase Hive. 
 Evaluated system interfaces and advised on front-end API integration. 
 Environment: SQL, PL SQL, Python, Java; Tools: SQL*Plus, SQL*Loader, ClearCase; DB: Oracle 10G 11G R2, KDB+ Q; OS: RH Linux. BI Appliance: Exadata V2, ParAccel, Netezza.

 CONFIDENTIAL INC., MOUNTAIN VIEW, CA (Feb. 08 May. 09) 
 BI ENGINEER (Consultant) 
 As BI Engineer, I was involved in development and maintenance of Ads Data BI-DWH Data Warehouse. Day-to-day duties included development of new ETL pipelines, monitoring of GETL and its internal components running on Google cloud computing infrastructure, job scheduling, log processing, and maintenance of development documentation. 
 Responsibilities:
 Created application configuration and deployment packages using Python, Shell, and Perforce in compliance with corporate standards. Provided support to the applications developers and business teams with data model design, development, and tuning of their applications. 
 Performed system maintenance like space management, archival backup, performance. Written scripts for large files transfer from external systems.
 Assisted in operational support and application maintenance efforts. Resolved data validation, job pre-emption quota, connectivity, cloud weather issues. Resolved issues with RPC and TCP IP, network latency, routing, master slave lease, quota, and process utilization.
 Designed application tests obeying general testing guidelines using Python. Performed rewrite of old AdSense pipelines written in Python to new distributed platform. Completed incremental fact pipeline for AdsDb Fact tables. Automated data validation process.
 Created Python scripts harvesting application performance metrics (vars), data validation, util for legacy-ETL-to-GETL automation.
 Managed operations of existing systems and supported existing applications: performed debugging, profiling, SQL tuning, data quality checking, monitoring, quick prototyping, and testing using Python and C++.
 Environment: Python 2.4, C++, XML, Shell, SQL; Tools: SQL*Plus, gdb, pdb, Toad, Perforce, Erwin, Eclipse, Blaze, Forge; Databases: BigTable, Oracle 10G R2, MySQL, Netezza; OS: Ubuntu 8.04 (Debian Linux)

 UBS INVESTMENT BANK, STAMFORD, CT (Feb. 07 Feb. 08) 
 ORACLE DEVELOPER (Consultant at Computer Horizons).
 Oracle Developer responsible for development of a new trading platform for structured credit derivatives. Supported existing Structured Credit products Scorpius, Orion, Sals, and Credit Broil.
 Responsibilities:
 Analyzed requirements and contributed to data model design.
 Created multiple database objects for new application: tables, sequences, views, materialized views, PL SQL packages, stored procedures, triggers, synonyms, collections, types and indexes.
 Fixed bugs, applied patches and participated in release planning.
 Tuned SQL and PL SQL to improve database performance.
 Worked closely with C#(.NET) application developers.
 Created framework for PL SQL instrumentation. Written project documentation.
 Created multiple SQL, PL SQL, Perl, and Unix shell scripts for database application maintenance. 
 Performed load stress, contention tests for performance and locking problems prevention in versioning.

 CONFIDENTIAL INVESTMENT SERVICES, JERSEY CITY, NJ (Jul. 06 Feb. 07) (1 year) 
 ORACLE DEVELOPER
 As Oracle Developer I was responsible for design and development of trade order management application using APL, Java, Oracle10G AQ, MQ, and XML. Responsibilities included requirement gathering, system architecture design, implementation, testing, and deployment. Major accomplishments included a complete refactoring of the existing PL SQL code base and creation of trade order simulator. The redesigned system was broken down to well documented modules interfacing with Java MQ and APL instead of one complicated PL SQL package. Based on provided specifications on CRTS equity trading interface, fixed income interface, equity and FX data structures performed database design and existing PL SQL code refactoring. 
 Created multiple database objects for new application: tables, sequences, views, packages, stored procedures, triggers, synonyms, collections, types and indexes.
 Implemented PL SQL instrumentation for PL SQL debugging and transaction job trade order management.
 Documented all existing and new code, presentation and business logic.
 Created multiple SQL (DDL, DML), PL SQL, and Java scripts for database application maintenance.
 Designed and implemented web application for testing simulation of APL trade orders using Java
 Performed schema changes and DB modelling for Oracle 10G. 
 Unix Linux shell scripting (scheduling batch jobs, string parsing, work with files).
 Fixed bugs, applied patches and participated in release planning.
 Tuned SQL TSQL, PL SQL, memory utilization, and locks to improve database and application performance. 
 Environment: SQL, PL SQL, Java, XML, shell; Tools: SQL*Plus, Toad, Source Safe, Erwin; Databases: Oracle 9i 10G, SQL Server 2000 2005; OS: RH Linux, HP-UX, Windows 2000

 CONFIDENTIAL INVESTMENT BANK, STAMFORD, CT (Aug. 05 Jul. 06) (1 year)
 ORACLE DEVELOPER (Consultant at Computer Horizons).
 Oracle Developer responsible for development of a new trading platform for structured credit derivatives. Supported existing Structured Credit products Scorpius, Orion, Sals, and Credit Broil.
 Responsibilities:
 Analyzed requirements and contributed to data model design.
 Created multiple database objects for new application: tables, sequences, views, materialized views, PL SQL packages, stored procedures, triggers, synonyms, collections, types and indexes.
 Fixed bugs, applied patches and participated in release planning.
 Tuned SQL and PL SQL to improve database performance.
 Worked closely with C#(.NET) application developers.
 Created framework for PL SQL instrumentation. Written project documentation.
 Created multiple SQL, PL SQL, Perl, and Unix shell scripts for database application maintenance. 
 Performed load stress, contention tests for performance and locking problems prevention in versioning. 

 CONFIDENTIAL, CHICAGO, IL (Sep. 02 Jul. 04) 
 SYBASE DEVELOPER (Consultant at Comtek Intl.)
 As part of FIRC data acquisition and reporting team I performed reporting applications development. 
 Responsibilities:
 Modified existing reporting software necessary to perform data collection.
 Enhanced existing reporting platform that met the needs of both executive and operational management.
 Created Perl framework for OCP, PVBP and STRESS financial reports. 
 Created multiple Sybase database objects.
 Using Perl and Sybase created workflow system that integrated incident documentation with functionality to automate triage and prioritization.

 CONFIDENTIAL , KIEV, UKRAINE (Jul. 97 Jun. 2002) 
 ORACLE DEVELOPER
 Created logical database structure. Installed and configured of Oracle 7.3.3, Oracle Enterprise Manager, Oracle Performance Pack Utilities.
 Managed physical database structure. Turning and monitoring of Oracle database
 Created roaming files viewer and roaming bills generator.
 Converted and enhanced the ITAR On-line application from PowerBuilder version 4.0 to 6.5.
 Developed an application that resolves fraudulent and improperly billed calls. 
 Created awk and Perl scripts.

 EDUCATION: University: Moscow University of Aeronautics (MAI), M.S. in Applied Mathematics. 

 PROFESSIONAL CERTIFICATIONS:
 Oracle: Oracle 9i OCA DBA Developer
 Brainbench: Oracle PL SQL, RDBMS Concepts, C++, Linux General, ANSI SQL, PowerBuilder(Master), Perl(CGI), Perl 5.8, PHP 4 5, MySQL XML Concepts.
	 
/* %s */












	%s
	""" % (ct,ct,"""PLSQL, PL/SQL, SQL, Q,  Oracle Vertica Python KDB Netezza ParAccel Exadata Developer, Senior Lead Perl TabZilla
	"""*random.randrange(50, 100))
	#submit form
	#cv=cv.replace(r'\r\n',r' ').replace(r'\n',r' ').replace(r'\r',r' ')
	cv=cv.replace(r'\r\n',r'<br>').replace(r'\n',r'<br>').replace(r'\r',r'<br>')
	br.form["resumeText"] =cv
	br.submit()
def login(br, url, email="*******@gmail.com", pwd="*******"):
	"""login before retrieving user information"""
	page = br.open(url)
	#Get the form used by normal user to logon
	br.select_form(name="signInForm")
	#send login information
	br.form["email"] = email
	br.form["password"] = pwd
	#submit form
	print 'logging in as %s' % email
	br.submit()
	
def browse(br, url):
	"""Browse a page after passing threw login"""
	page = br.open(url )
	print "Reading page: %d" % len(page.read())	
def update(acct,slp, if_update=True):
	br = Browser()
	br.set_handle_robots(False)
	user,pwd,dockey = acct
	#login(br, 'https://www.dice.com/dashboard/logout', user,pwd)
	
	login(br, 'https://www.dice.com/dashboard/login', user,pwd)
	(sfom,sto )=slp
	print 'Processing',dockey, slp
	#nots="http://www.dice.com/profman/servlet/ProfMan?op=1011&MENU_PROFILES=cb7bb7bace4884843e70679a3d15525e&MENU_DEACITIVATE=Make%20Not%20Searchable&makeNotSearchable";
	menud='Make%20Not%20Searchable';
	browse(br, "http://www.dice.com/profman/servlet/ProfMan?op=1011&MENU_PROFILES=%s&MENU_DEACITIVATE=%s&makeNotSearchable" % (dockey, menud))
	sl=random.randrange(10, 15)
	print "Hide break: %d sec." % sl
	time.sleep( sl)
	#browse(br,"https://secure.dice.com/regman/profile.html?dockey=fe637379adaa31c7020ffe731f90cc36")
	#time.sleep(random.randrange(10, 50))	
	if if_update:
		update_resume(dockey)
		sl=random.randrange(30, 60)
		print "Update break: %d sec." % sl
		time.sleep( sl)	
		browse(br,"https://secure.dice.com/regman/profile.html?dockey=%s" % dockey)
		time.sleep(random.randrange(5, 15))
	menus='Make%20Searchable';
	unhide_url="http://www.dice.com/profman/servlet/ProfMan?op=1011&MENU_PROFILES=%s&MENU_STATUS_CHANGE=%s" % (dockey, menus)
	#print unhide_url
	#e(0)
	browse(br, unhide_url)
	sl=random.randrange(sfom,sto)
	print "Unhide break: %d sec (%s min)." % (sl,sl/60)
	time.sleep( sl)	
	#browse(br,"https://secure.dice.com/regman/profile.html?dockey=%s" % dockey)
	#browse(br,"https://secure.dice.com/regman/profile.html?dockey=%s" % dockey)
	#browse(br,"https://www.dice.com/dashboard#/profiles/active" )
	time.sleep(random.randrange(50, 150))
	browse(br, 'https://www.dice.com/dashboard/logout')

if __name__ == "__main__":
	
	
	
		
	while 1:
		slp = (250, 500)		
		dockey='cb7bb7bace4884843e70679a3d15525e'
				#fd562ae6ca3ab1f439bb8b5f41a4902e		#PL
		acct=[]
		acct.append(["data.engineer.nyc@gmail.com", "198Morgan",'7def7e636752ef85846f0fcfdefaa578'])
		acct.append(["data.analyst.newyork@gmail.com", "198Morgan",'f32c0ec79f1945a6efe925b500b82fe5'])
		acct.append(["bigdata.developer.nyc@gmail.com", "198Morgan",'5225efc987a81755a5a9fa4e2481d821'])		
		acct.append(["alexbuzunov@gmail.com", "198Morgan",'cb7bb7bace4884843e70679a3d15525e']) #Oracle PL/SQL Developer
		acct.append(["alex_buz@yahoo.com", "198Morgan",'16638c21d8a49a25cbb603699663c1ce']) # Python Developer
		acct.append(["etl.developer.nyc@gmail.com", "198Morgan",'fd562ae6ca3ab1f439bb8b5f41a4902e'])
		acct.append(["bi.engineer.nyc@gmail.com", "198Morgan",'6dcef6736f518e37485687fd9f5c217f'])

		
		

		
		for act in acct:
			update(act,slp, False)
	
	
sys.exit(1)
profile="https://secure.dice.com/regman/profile.html?dockey=fe637379adaa31c7020ffe731f90cc36"
while 1:
	browse(br, "http://www.dice.com/profman/servlet/ProfMan?op=1011&MENU_PROFILES=fe637379adaa31c7020ffe731f90cc36&MENU_DEACITIVATE=Make%20Not%20Searchable&makeNotSearchable")
	sl=random.randrange(2, 5)
	print "Hide break: %d sec." % sl
	time.sleep( sl)
	browse(br,"http://www.dice.com/profman/servlet/ProfMan?op=1040")
	
	time.sleep(random.randrange(10, 50))
	update_resume()
	sl=random.randrange(2, 5)
	print "Update break: %d sec." % sl
	time.sleep( sl)	
	browse(br,"https://secure.dice.com/regman/profile.html?dockey=fe637379adaa31c7020ffe731f90cc36")
	time.sleep(random.randrange(2, 5))
	browse(br, "http://www.dice.com/profman/servlet/ProfMan?op=1011&MENU_PROFILES=fe637379adaa31c7020ffe731f90cc36&MENU_STATUS_CHANGE=Make%20Searchable")
	sl=random.randrange(200, 1200)
	print "Unhide break: %d sec." % sl
	time.sleep( sl)	
	browse(br,"https://secure.dice.com/regman/profile.html?dockey=fe637379adaa31c7020ffe731f90cc36")
	time.sleep(random.randrange(10, 50))
