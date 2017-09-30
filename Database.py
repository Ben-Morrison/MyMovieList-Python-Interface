import mysql.connector

class Database:
	def __init__(self, dbserver, dbname, dbuser, dbpassword):
		self.connected = False
		try:
			self.connection = mysql.connector.connect(user=dbuser, password=dbpassword, host=dbserver, database=dbname)
			self.connected = True
		except mysql.connector.Error as e:
			raise e
		return
	
	def getConnection(self):
		if self.connected == True:
			return self.connection
		else:
			return False
		
	def executeQuery(self, query):
		try:
			if self.connected == True:
				cursor = self.connection.cursor()
				cursor.execute(query)
				return cursor
			else:
				raise Exception("There is no connection to the database")
		except mysql.connector.Error as e:
			raise e
		return
			
	def closeConnection(self):
		if self.connected == True:
			self.connection.close()
			self.connected = False
		return