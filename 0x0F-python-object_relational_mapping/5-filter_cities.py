#!/usr/bin/python3
"""
Display all cities in states from the database hbtn_0e_4_usa

"""

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

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    print(rows)

    print(', '.join(row[0]for row in rows))

    cursor.close()
    db.close()
