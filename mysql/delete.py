import mysql.connector as mysql

db = mysql.connect(host='localhost', port=3306, user='root', passwd='root', database='testdb')

cursor = db.cursor()

delete_stm = 'DELETE FROM students WHERE id = 1'

cursor.execute(delete_stm)

db.commit()