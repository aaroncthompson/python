# slightly less simple messageboard

# import datetime modules so i can timestamp messages
from datetime import datetime,timezone

# import path so i can call my modules
from sys import path
# import my modules
path.append('modules')
import file_io as fio
import message_bank as mb

messages = []

def welcome():
    """Allows user to choose what they'd like to do."""
    while True:
        print(f"Welcome to the messageboard! It is currently {datetime.now(timezone.utc)}.\nThere are {len(mb.messages)} messages.")
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
    """Requests user input to construct a dictionary entry. Appends it to messageboard in memory and writes total to file."""
    entry = {}
    entry['name'] = input("What is your name? >> ").title()
    if entry['name'].lower() == "bob":
        print(f"Bob isn't supposed to be using this.\nThis incident will be reported.")
    entry['date'] = str(datetime.now(timezone.utc))
    entry['message'] = input("What is your message? >> ")
    mb.messages.append(entry)
    fio.write_file(mb.messages)

def show_messages():
    """Reloads file, lists messages."""
    fio.load_file()
    for each_message in mb.messages:
        if "bob" in each_message['name'].lower() or "bob" in each_message['message'].lower():
            print("A message mentioning Bob has been removed.")
            continue
        print(f"{each_message['name']} said at {each_message['date']}: {each_message['message']}")

# actual operation
fio.load_file()
welcome()

# planned: don't have an entire module just for one variable
# planned: refactoring
# planned: allow user to selectively display messages based on certain criteria
