import mysql.connector as mysql

db = mysql.connect(host='localhost', port=3306, user='root', passwd='root', database='testdb')

cursor = db.cursor()

cursor.execute('SELECT * FROM students where age >= 30')

students = cursor.fetchall()

# return only one record
# stud = cursor.fetchone()
# print(stud)
print(students)
for student in students:
    print('ID:: ', student[0])
    print('Name:: ', student[1])
