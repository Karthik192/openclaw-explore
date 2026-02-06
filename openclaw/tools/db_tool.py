import sqlite3

def run_sql(query: str):
    try:
        conn = sqlite3.connect("demo.db")
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"DB_ERROR: {e}"
