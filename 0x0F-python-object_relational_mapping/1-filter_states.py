#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <dbname>")
        sys.exit(1)

    db_n = sys.argv[3]
    un = sys.argv[1]
    pw = sys.argv[2]
    lh = 'localhost'

    try:
        db = MySQLdb.connect(host=lh, port=3306, user=un, passwd=pw, db=db_n)
        cursor = db.cursor()
        qy = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(qy)
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f'Error connecting to MySQL: {e}')
        sys.exit(1)
