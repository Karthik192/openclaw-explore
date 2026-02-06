from tools.db_tool import run_sql

def is_safe(query: str) -> bool:
    forbidden = ["delete", "update", "drop", "insert", "alter"]
    return not any(word in query.lower() for word in forbidden)

def handle_query(sql: str):
    if not is_safe(sql):
        return "❌ Destructive queries are not allowed."

    result = run_sql(sql)
    return result
