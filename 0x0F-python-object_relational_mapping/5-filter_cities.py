#!/usr/bin/python3

import MySQLdb
import sys


keywords = ["TRUNCATE", "TABLE", "SELECT", "WHERE", "FROM"]

def sanitize(string: str) -> str:
    for r in "@#%;*='\"&^!$%^(){[]}":
        string = string.replace(r, '')
    for k in keywords:
        string = string.replace(k, f'"{k}"')
        string = string.replace(k.lower(), f'"{k.lower()}"')

    return string   
    
def main():
    uname, passw, db_name, s_name = sys.argv[1:]
    connection = MySQLdb.connect(host="localhost", port=3306,
            user=uname, passwd=passw, db=db_name)
    cursor = connection.cursor()

    cursor.execute("SELECT cities.name from cities INNER JOIN states ON cities.state_id=states.id WHERE states.name='{}'".format(sanitize(s_name))
    )

    query_rows = cursor.fetchall()
    print(", ".join(row[0] for row in query_rows))
    

    cursor.close()
    connection.close()
    

if __name__ == "__main__":
    main()
