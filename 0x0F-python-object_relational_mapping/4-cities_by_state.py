#!/usr/bin/python3
"""script for use in getting all states from sql db
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 4:
        print("Usage: {} username password db_name".format(args[0]))
        exit(1)
    username = args[1]
    password = args[2]
    data = args[3]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data,
                         port=3306)
    cur = db.cursor()
    num_rows = cur.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        ''')
    rows = cur.fetchall()
    for row in rows:
        print(row)
