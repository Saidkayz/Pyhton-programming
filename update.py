import sqlite3

conn = sqlite3.connect('acer.db')
print("Opended database successfully")

conn.execute("UPDATE EMPLOYEE set SALARY = 80000.00 where id = 1")
conn.commit()

cursor = conn.execute("SELECT id,name,address,salary from EMPLOYEE")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2])
    print("ADDRESS = ", row[3])
    print("SALARY = ", row[4])
print("Operation done successfully")
conn.close()