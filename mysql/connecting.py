import mysql.connector as mysql

db = mysql.connect(host='localhost', port=3306, user='root', passwd='root', database='testdb')

# Get a handle
cursor = db.cursor()

cursor.execute("SHOW DATABASES")

for database in cursor:
    print(database)