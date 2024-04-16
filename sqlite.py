import sqlite3

## Connect to SQlite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table

cursor=connection.cursor()

## Create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

cursor.execute(table_info)


## Insert Some more records

cursor.execute("""Insert Into STUDENT values ('Clinton', 'Computer Science', 'A')""")
cursor.execute("""Insert Into STUDENT values ('Victory', 'Government', 'B')""")
cursor.execute("""Insert Into STUDENT values ('Stephanie', 'Nursing', 'A')""")
cursor.execute("""Insert Into STUDENT values ('Martha', 'Medicine', 'B')""")
cursor.execute("""Insert Into STUDENT values ('Virtue', 'Computer Science', 'B')""")


## Display all the records

print("The Inserted records are")
data = cursor.execute("""Select * from STUDENT""")
for row in data:
    print(row)


## Commit your changes in the database
connection.commit()
connection.close()