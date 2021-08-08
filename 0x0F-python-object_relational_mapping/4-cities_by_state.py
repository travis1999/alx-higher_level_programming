#!/usr/bin/python3
"""cities by state"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: ./0-select_states.py username password database")
        exit()

    with MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306) as db:
        cursor = db.cursor()
        cursor.execute("SELECT cities.id, cities.name, states.name \
FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id")
        for unit in cursor.fetchall():
            print(unit)
