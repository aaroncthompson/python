# slightly less simple messageboard
# not yet functional, let me figure out how to save/load dictionaries to file first

# import datetime modules so i can timestamp messages
from datetime import datetime,timezone

# import sys so i can call my modules
import sys
# import my modules
sys.path.append('modules')
import modules/file_io as f_io

def welcome():
    while True:
        print(f"Welcome to the messageboard! It is currently {datetime.now(timezone.utc)}.\nThere are {len(messages)} messages.")
        choice = input('Type "save" (without quotes) to save a message, "show" (without quotes) to list the messages saved so far, or "exit" to exit.\n>> ')
        if choice == "save":
            save_message()
        elif choice == "show":
            show_messages()
        elif choice == "exit":
            print("Exiting!")
            break
        elif choice == "quit":
            print("I know you meant 'exit', so I'll respect that. Exiting!")
            break
        else:
            print(f"Invalid choice.\n")

def save_message():
    entry = {}
    entry['name'] = input("What is your name? >> ").title()
    if entry['name'].lower() == "bob":
        print(f"Bob isn't supposed to be using this.\nThis incident will be reported.")
    entry['date'] = str(datetime.now(timezone.utc))
    entry['message'] = input("What is your message? >> ")
    messages.append(entry)

def show_messages():
    for each_message in messages:
        if "bob" in each_message['name'].lower() or "bob" in each_message['message'].lower():
            print("A message mentioning Bob has been removed.")
            continue
        print(f"{each_message['name']} said at {each_message['date']}: {each_message['message']}")

# actual operation
f_io.load_file()
welcome()

# 3.0 should allow the user to selectively display messages from a certain date (let's just stick to month/day) and/or name
# 4.0 should actually save the messages somewhere and have them persist
