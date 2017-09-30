import mysql.connector

class Movie:
	def __init__(self, title, summary):
		self.title = title
		self.summary = summary
		
	def displayMovie(self):
		print(self.title)
		return