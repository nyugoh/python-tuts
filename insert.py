import mysql.connector as mysql

db = mysql.connect(host='localhost', port=3306, user='root', passwd='root', database='testdb')

cursor = db.cursor()

insert_stm = 'INSERT INTO students VALUES(%s, %s, %s)'

cursor.execute(insert_stm, [10, 'Jane Doe', 20])

students = [ [2, 'John Doe', 30], [3, 'Mary Fisher', 40], [4, 'Sunny James', 35]]
cursor.executemany(insert_stm, students)

db.commit()