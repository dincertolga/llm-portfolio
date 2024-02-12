import sqlite3

## Connect to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record and create a table

cursor=connection.cursor()

## create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

## Insert records

cursor.execute('''Insert Into STUDENT values('Tolga','Electrical Engineering','A',90)''')
cursor.execute('''Insert Into STUDENT values('Morgoth','Computer Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Elendil','Electrical Engineering','A',86)''')
cursor.execute('''Insert Into STUDENT values('Aragorn','Data Science','A',50)''')
cursor.execute('''Insert Into STUDENT values('Feanor','Data Science','A',35)''')

## display the records

print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()
