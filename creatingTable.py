import MySQLdb

db = MySQLdb.connect("localhost","root","","python" )
cursor = db.cursor()
sql = """CREATE TABLE Student1(
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         GENDEER CHAR(1),
         ENROLLMENT INT(12))"""

cursor.execute(sql)
db.close()