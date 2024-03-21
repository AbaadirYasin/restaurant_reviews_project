import sqlite3

class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def fanciest(cls):
        with sqlite3.connect("restaurant_reviews.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM restaurants ORDER BY price DESC LIMIT 1")
            result = cursor.fetchone()
            if result:
                return result[0]  
            return None
