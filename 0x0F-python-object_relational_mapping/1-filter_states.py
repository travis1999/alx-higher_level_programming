#!/usr/bin/python3

import MySQLdb
import sys

def main():
    uname, passw, db_name = sys.argv[1:]
    connection = MySQLdb.connect(host="localhost", port=3306,
            user=uname, passwd=passw, db=db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    connection.close()
    

if __name__ == "__main__":
    main()
