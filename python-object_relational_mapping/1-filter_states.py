#!/usr/bin/python3
"""
script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def list_states_starting_with_N(username, password, database):
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=database)
        with db.cursor() as cursor:
            cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' \
                            ORDER BY id ASC")
            states = cursor.fetchall()
            for state in states:
                print(state)
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        list_states_starting_with_N(username, password, database)
    else:
        print("Usage: python3 script.py <username> <password> <database>")
