#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 14-model_city_fetch_by_state.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    try:
        # Query to fetch all City objects
        cities = session.query(City).join(State).order_by(City.id).all()

        # Print results as required
        for city in cities:
            print(f"{city.state.name}: ({city.id}) {city.name}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close the session
        session.close()