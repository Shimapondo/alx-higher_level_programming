#!/usr/bin/python3
"""
    python3 -c 'print(__import__("my_module").__doc__)'
"""


if __name__ == '__main__':
import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]


cnx = MySQLdb.connect(user=mysql-username, password=mysql_password, host ='localhost', database=database_name, port=3306)

cursor = cnx.cursor()
query = ("SELECT * FROM states ORDER BY id ASC")
cursor.execute(query)


for (state,) in cursor:
    print(state)


cursor.close()
cnx.close()
