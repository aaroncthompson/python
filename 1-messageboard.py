# simple messageboard

from datetime import datetime,timezone

# first!
messages = [{'name': 'Aaron', 'date':'2022-06-22 05:07:20.884325+00:00', 'message':'Hey there! Hope you\'re having a pretty okay day.'}]

def welcome():
    while input != "exit":
        print(f"Welcome to the messageboard! It is currently {datetime.now(timezone.utc)}.\nThere are {len(messages)} messages.")
        choice = input('Type "save" (without quotes) to save a message, "show" (without quotes) to list the messages saved so far, or "exit" to exit.\n>> ')
        if choice == "save":
            save_message()
        elif choice == "show":
            show_messages()
        elif choice == "exit":
            print("Exiting!")
        else:
            print("Invalid choice.")

def save_message():
    entry = {}
    entry['name'] = input("What is your name? >> ").title()
    if entry['name'].lower() == "bob":
        print(f"Bob isn't allowed to use this.\nThis incident will be reported.")
    entry['date'] = str(datetime.now(timezone.utc))
    entry['message'] = input("What is your message? >> ")
    messages.append(entry)

def show_messages():
    for each_message in messages:
        print(f"{each_message['name']} said at {each_message['date']}: {each_message['message']}")

welcome()



# 3.0 should allow the user to selectively display messages from a certain date (let's just stick to month/day) and/or name
# 4.0 should actually save the messages somewhere and have them persist
