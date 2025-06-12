from book_recommender import get_book_recommendation
from scheduler import schedule_meeting, send_reminder
from discussion import generate_discussion_prompt, summarize_chapter
from platform_adapter import send_message, listen_for_commands

def handle_command(command, args):
    if command == "recommend":
        book = get_book_recommendation(args)
        send_message(f"Recommended book: {book}")
    elif command == "schedule":
        info = schedule_meeting(args)
        send_message(f"Meeting scheduled: {info}")
    elif command == "remind":
        reminder = send_reminder(args)
        send_message(f"Reminder sent: {reminder}")
    elif command == "prompt":
        prompt = generate_discussion_prompt(args)
        send_message(f"Discussion prompt: {prompt}")
    elif command == "summarize":
        summary = summarize_chapter(args)
        send_message(f"Summary: {summary}")
    else:
        send_message("Unknown command.")

if __name__ == "__main__":
    listen_for_commands(handle_command)