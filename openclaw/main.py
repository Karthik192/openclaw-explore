from claws.sql_claw import handle_user_input

print("🦾 OpenClaw SQLite Agent (NL → SQL)")
print("Ask questions in English. Type exit to quit.\n")

while True:
    user_input = input("You> ")
    if user_input.lower() == "exit":
        break

    result = handle_user_input(user_input)
    print("Result:", result)
