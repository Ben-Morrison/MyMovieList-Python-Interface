from Movie import *
from User import *
from Database import *

import sys
import getpass
import mysql.connector

dbserver = "192.168.1.3"
dbname = "mymovielist_db"
dbuser = "user_defaultddd"
dbpassword = "password"

conn = None

running = False

try:
	conn = Database(dbserver, dbname, dbuser, dbpassword)
	running = True
except Exception as e:
	print(e)

menuMain = ["1. Users", "2. Movies", "3. People", "4. Other", "9. Exit"];
userInput = 0

def menuUserAdd():
	"Menu for adding a User to the database"

	username = None
	password1 = None
	password2 = None
	email = None

	looping = True
	while looping == True:
		username = input("Enter a username")
		
		try:
			result = User.validateUsername(conn, username)
			if result == True:
				print("Username already exists")
			else:
				print("User can be added")
				looping = False
		except Exception as e:
			print(e)
			
	looping = True
	while looping == True:
		password1 = input("Enter a password")
		password2 = input("Confirm your password")
		
		if password1 != password2:
			print("Your passwords must match")
		if password1 == password2:
			looping = False

	looping = True
	while looping == True:
		email = input("Enter an email address")
		
		try:
			result = User.validateEmail(conn, email)
			if result == True:
				print("Email already exists")
			else:
				print("Email is valid")
				looping = False
		except Exception as e:
			print(e)

	try:
		User.addUser(conn, username, password1, email)
		print("User successfully added")
	except Exception as e:
		print(e)
		
	return
	
def menuUserQuery():
	query = input("Enter a condition")
	
	try:
		users = User.queryUser(conn, query)
		print("-------------")
		print("Listing Users")
		User.displayUsers(users)
		print("-------------")
	except Exception as e:
		print(e)
	return

def menuUser():
	print("User Menu")
	menu = ["1. List All", "2. List Users with Condition", "3. Add User", "9. Back"];
	
	looping = True
	
	while looping:
		for x in range(0, len(menu)):
			print (menu[x])
			
		userInput = input("")
		
		if userInput == '1':
			try:
				Users = User.getUsers(conn)
				print("-------------")
				print("Listing Users")
				for x in Users:
					x.displayUser()
				print("-------------")
			except mysql.connector.Error as e:
				print("There was an error with the Database")
		elif userInput == '2':
			menuUserQuery()
		elif userInput == '3':
			menuUserAdd()
		elif userInput == '9':
			looping = False
		else:
			print("Enter a valid option")
	return

while running:
	print("Welcome to the Python interface for MyMovieList")
	
	for x in range(0, len(menuMain)):
		print (menuMain[x])
		
	userInput = input("")
	
	if userInput == '1':
		menuUser()
	elif userInput == '2':
		print("Movies")
	elif userInput == '3':
		print("People")
	elif userInput == '4':
		print("Other")		
	elif userInput == '9':
		conn.closeConnection()
		running = False
		#sys.exit()	
	else:
		print("Enter a valid option")
		
