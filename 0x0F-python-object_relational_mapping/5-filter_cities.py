#!/usr/bin/python3
"""script for use in getting all states from sql db
"""
import MySQLdb
import sys


if __name__ == '__main__':
    args = sys.argv
    if len(args) < 5:
        print("Usage: {} username password db_name state_name".format(args[0]))
        exit(1)

    # connect to database and set up user input variables
    username = args[1]
    password = args[2]
    data = args[3]
    statename = args[4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=data,
                         port=3306)
    cur = db.cursor()
    # execute sql join statement to gather states and cities
    num_rows = cur.execute('''
        SELECT cities.id, cities.name, states.name
        FROM cities INNER JOIN states
        ON cities.state_id=states.id
        ORDER BY cities.id ASC
        ''')
    rows = cur.fetchall()
    # get cities from all rows matching state name
    cities = [row[1] for row in rows if statename == row[2]]
    num_cities = len(cities)
    # print cities out using custom ends to format output
    for i, city in enumerate(cities):
        if i == num_cities - 1:
            print(city)
        else:
            print(city, end=", ")
