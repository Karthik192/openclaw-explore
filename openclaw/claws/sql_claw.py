import requests
from tools.db_tool import run_sql

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

def load_system_prompt():
    with open("system/instructions.txt", "r") as f:
        return f.read()

def generate_sql(user_input: str) -> str:
    system_prompt = load_system_prompt()

    prompt = f"""
    {system_prompt}

    User request:
    {user_input}

    Respond with ONLY the SQL query.
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()

def is_safe(sql: str) -> bool:
    forbidden = ["delete", "update", "drop", "insert", "alter"]
    return not any(word in sql.lower() for word in forbidden)

def handle_user_input(user_input: str):
    sql = generate_sql(user_input)

    print(f"\n🧠 Generated SQL:\n{sql}\n")

    if not is_safe(sql):
        return "❌ Destructive queries are not allowed."

    return run_sql(sql)
