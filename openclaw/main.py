from claws.sql_claw import handle_query

print("🦾 OpenClaw SQLite Agent")
print("Type SQL directly (for now). Type exit to quit.\n")

while True:
    user_input = input("SQL> ")
    if user_input.lower() == "exit":
        break

    output = handle_query(user_input)
    print("Result:", output)
