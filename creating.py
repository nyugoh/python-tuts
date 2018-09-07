import mysql.connector as mysql

db = mysql.connect(host='localhost', port='3306', user='root', passwd='root', database='testdb')

cursor = db.cursor() # RETURN A HANDLE FOR ALL THE DBS

cursor.execute("CREATE DATABASE IF NOT exists testdb")
cursor.execute("SHOW DATABASES")
for cur in cursor:
    print(cur)

cursor.execute('CREATE TABLE students (id INT PRIMARY KEY,name VARCHAR(255) NOT NULL, age INT NOT NULL)')
cursor.execute('SHOW TABLES')

print('List of tables')
for tb in cursor:
    print(tb)