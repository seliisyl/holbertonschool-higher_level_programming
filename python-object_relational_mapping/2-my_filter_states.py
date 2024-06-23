#!/usr/bin/python3
"""
Script that filters states by user input from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def filter_states_by_name(username, password, database, state_name):
    try:
        # Connect to the database
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database
        )
        cursor = db.cursor()

        # Execute the query to filter states by name
        query = ("SELECT id, name FROM states WHERE name = %s "
                 "ORDER BY id ASC")
        cursor.execute(query, (state_name,))

        # Fetch all the results
        states = cursor.fetchall()

        # Display the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close the cursor and the connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
        state_name = sys.argv[4]
        filter_states_by_name(username, password, database, state_name)
    else:
        print("Usage: python3 2-my_filter_states.py <username> <password> "
              "<database> <state name>")
