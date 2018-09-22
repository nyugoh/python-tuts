import mysql.connector as mysql

db = mysql.connect(host='localhost', port=3306, user='root', passwd='root', database='testdb')

cursor = db.cursor()

cursor.execute('UPDATE students SET name="Sunnery James" where id=4')
cursor.execute('SELECT * FROM  students order by age DESC')
students = cursor.fetchall()

print(students)
for student in students:
    print('ID:: ', student[0])
    print('Name:: ', student[1])

db.commit()