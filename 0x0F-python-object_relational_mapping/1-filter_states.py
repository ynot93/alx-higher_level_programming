#!/usr/bin/python3
"""
Lists all states in the database hbtn_0e_0_usa whose name
starts with N

"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database = sys.argv[1:]

    db_config = {
            'host': 'localhost',
            'port': 3306,
            'user': username,
            'passwd': password,
            'db': database
    }

    db = MySQLdb.connect(**db_config)

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
