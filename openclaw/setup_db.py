# setup_db.py
import sqlite3

conn = sqlite3.connect("demo.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
    category TEXT
)
""")

cur.executemany(
    "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
    [
        ("Laptop", 80000, "Electronics"),
        ("Phone", 50000, "Electronics"),
        ("Chair", 3000, "Furniture"),
        ("Table", 7000, "Furniture"),
        ("Headphones", 2000, "Electronics")
    ]
)

conn.commit()
conn.close()
