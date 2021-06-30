from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from models import (Base, session,
					Book, engine)
import datetime
import csv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://har_data.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #suppresses warning
db = SQLAlchemy(app)

def clean_date(date_str):
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	split_date = date_str.split(' ')
	print(split_date)
	month = int(months.index(split_date[0]) + 1)
	day = split_date[1].split(',')[0]
	print(day)
	datetime.date()
def add_csv():
	with open('suggested_books.csv') as csvfile:
			data = csv.reader(csvfile)
			for row in data:
				print(row)
#function declarations
def menu():
	while True:
		print('''
			\nReading Options
			\r1) Register
			\r2) Start reading
			\r3) Pick skill level
			\r4) Pick reading interest
			\r5) Exit

			''')
		choice = input("WHat would you like to do?")
		if choice in ('1','2','3','4','5'):
			return choice
		else:
			input('''
				\rPlease choose one of the options above.
				\rA number from 1-5.
				\rThen press enter.
				''')



#some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
    return "Lord have mercy!"

def app():
	app_running = True
	while app_running:
		choice = menu()
		if choice == '1':
			pass
		elif choice == '2':
			pass
		elif choice == '3':
			pass
		elif choice == '4':
			pass
		else:
			print("Goodbye!")
			app_running = False


if __name__ == "__main__":
	Base.metadata.create_all(engine)
	# app()
	# add_csv()
	clean_date('October 13, 1987')
