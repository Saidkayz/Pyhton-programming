import sqlite3

conn = sqlite3.connect('acer.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(1,'Jeff',33,'Carlifonia',45000.00)")
conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(2,'Mark',30,'Norway',15000.00)")
conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(3,'John',39,'Texas',145000.00)")
conn.execute("INSERT INTO EMPLOYEE(ID, NAME, AGE, ADDRESS, SALARY)\
 VALUES(4,'James',63,'Kenya',25000.00)")
conn.commit()
print("Records created successfully")
conn.close()