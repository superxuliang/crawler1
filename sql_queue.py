


import traceback
from xlutils import *
from queue_base import * 

class SQLQueue(Queue):
	def __init__(self,queue_name):
		import MySQLdb

		
		self.conn = MySQLdb.connect(host="localhost", user="root", passwd="abcd850211")
		self.cursor = self.conn.cursor()

		db_name = "crawler_queue"
		tb_name = "que_" + queue_name
		self.db_name = db_name
		self.tb_name = tb_name

		try:
			self.conn.select_db(db_name)
		except:
			print traceback.format_exc()
			self.cursor.execute("create database " + db_name)
			self.conn.select_db(db_name)

		bExists = False
		try:
			self.cursor.execute("show tables like '%s'" % self.tb_name)
			results = self.cursor.fetchall()
			#log("=-----------")
			#log(results)

			if len(results) > 0:
				bExists = True
		except:
			print traceback.format_exc()
			pass

		if  not(bExists):
			s = """create table %s (
				id int, 
				link varchar(760) not null, 
				priority int, 
				status varchar(20), 
				infos varchar(20000), 
				gmt_modified TIMESTAMP,
				PRIMARY KEY (link)
				); """
			self.cursor.execute(s % tb_name)
			self.conn.commit()

		#log(self.tb_name)


	def find(self, x):
		s = """
			select * from %s where link like '%s'
			"""
		try:
			self.cursor.execute(s % (self.tb_name, str(x)))
			return(len(self.cursor.fetchall()) > 0)

		except:
			print traceback.format_exc()
			sys.stderr.write("ERROR: in find %s \n" % str(x))
		
		return(False)


	def popItems(self, nCount = 1000):
		s = """
			select link from %s where (status = 'new' or status is null) limit %d
			"""

		try:
			#log(self.tb_name)
			self.cursor.execute(s % (self.tb_name,nCount))

			results = self.cursor.fetchall()
			if len(results) == 0:
				return ([])
			arr = []
			for x in results:
				arr.append(x[0])
			return(arr)
		except:
			print traceback.format_exc()
		return([])


	def putItems(self,arr= []):

		s = """
			replace into %s values(1,'%s',0,'new','',now())
			"""

		try:
			for i in range(0,len(arr)):
				self.cursor.execute(s % (self.tb_name, arr[i]))
			self.conn.commit()

			return(True)
		except:
			print traceback.format_exc()

		return(False)

	def eraseItems(self, arr = []):
		return(True)

