# Placeholder for Slack/Discord/Web integration.
# For CLI demo, we use input() and print().

def start_bot(command_handler):
    print("AI Book Club Host Bot Started. Type a command (recommend, schedule, remind, prompt, summarize) or 'quit'.")
    while True:
        inp = input(">> ")
        if inp.lower() == "quit":
            print("Goodbye!")
            break
        parts = inp.strip().split(" ", 1)
        command = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        user = "demo_user"
        response = command_handler(command, args, user)
        print(response)