import mysql.connector

class User:
	def __init__(self, id, username, password, email):
		self.id = id
		self.username = username
		self.password = password
		self.email = email
		
	def displayUser(self):
		print(str(self.id) + ", " + self.username + ", " + self.password + ", " + self.email)
		return
		
	@staticmethod
	def displayUsers(users):
		for x in users:
			x.displayUser()
		return
		
	@staticmethod
	def validateUsername(conn, username):
		"Checks the database for the given User, returns true or false"
		
		query = "SELECT * FROM User WHERE userName = '" + username + "';"
		
		try:
			result = conn.executeQuery(query)
			rows = result.fetchall()
		except Exception as e:
			raise e

		if result.rowcount > 0:
			return True
		else:
			return False
			
	@staticmethod
	def validateEmail(conn, email):
		"Checks the User table for a record with the given email address, returns true or false"
		
		query = "SELECT * FROM User WHERE email = '" + email + "';"
		
		try:
			result = conn.executeQuery(query)
			rows = result.fetchall()
		except Exception as e:
			raise e
		
		if result.rowcount > 0:
			return True
		else:
			return False
			
	@staticmethod
	def getUsers(conn):
		"Returns a list of User Objects"
		
		query = "SELECT * FROM User"
	
		try:
			result = conn.executeQuery(query)
			
			Users = []
			for x in result:
				u = User(x[0], x[1], x[2], x[3])
				Users.append(u)
			
			return Users
		except mysql.connector.Error as e:
			raise e
		return
		
	@staticmethod
	def queryUser(conn, condition):
		"Executes a query with a condition on the User table, returns User objects"
		
		query = "SELECT * FROM User WHERE " + condition

		try:
			result = conn.executeQuery(query)
			
			Users = []
			for x in result:
				u = User(x[0], x[1], x[2], x[3])
				Users.append(u)
			
			return Users
		except Exception as e:
			raise e
		return
			
	@staticmethod
	def addUser(conn, username, password, email):	
		"Adds a User to the database"
	
		#Change this to get the current date
		date = '2017-01-01'
		
		try:
			query = "INSERT INTO User VALUES (NULL, '" + username + "', '" + password + "', '" + email + "', '" + date + "')"
			result = conn.executeQuery(query)
		except Exception as e:
			raise e
		return