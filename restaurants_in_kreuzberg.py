## simple demo script for showing how to connect to an sqlite DB 
# from Python, and run a simple SQL query 

# import the python library for SQLite 
import sqlite3

# connect to the database file, and create a connection object
db_connection = sqlite3.connect('restaurants.db')

# create a database cursor object, which allows us to perform SQL on the database. 
db_cursor = db_connection.cursor()

# run a first query 
db_cursor.execute("SELECT name FROM restaurants WHERE neighborhood_id='1';")

# store the result in a local variable. 
# this will be a list of tuples, where each tuple represents a row in the table
list_neighborhoods = db_cursor.fetchall()

print("list_restaurants contents:")
print(list_neighborhoods)
#Get a list of all the restaurants in Berlin in the database, listing their neighborhood. 


db_connection.close()
