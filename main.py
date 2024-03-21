# main.py

import sqlite3
from models import Restaurant

def create_restaurants():
    # Connect to the database
    conn = sqlite3.connect("restaurant_reviews.db")
    cursor = conn.cursor()

    # Create restaurants table if not exists
    cursor.execute("CREATE TABLE IF NOT EXISTS restaurants (id INTEGER PRIMARY KEY, name TEXT NOT NULL, price INTEGER NOT NULL)")

    # Sample restaurant data
    restaurant_data = [
        ("ABC Restaurant", 3),
        ("XYZ Restaurant", 5)
    ]

    # Insert restaurants into the database
    cursor.executemany("INSERT INTO restaurants (name, price) VALUES (?, ?)", restaurant_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

def main():
    # Create restaurants in the database
    create_restaurants()

    # Test the Fanciest Restaurant functionality
    print("Fanciest Restaurant:", Restaurant.fanciest())

if __name__ == "__main__":
    main()
