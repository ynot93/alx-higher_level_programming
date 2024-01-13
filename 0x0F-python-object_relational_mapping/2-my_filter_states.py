#!/usr/bin/python3
"""Display all valuues in states where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database, state_name = sys.argv[1:]

    db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': username,
            'passwd': password,
            'db': database
    }

    db = MySQLdb.connect(**db_config)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
