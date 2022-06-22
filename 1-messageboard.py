# simple messageboard

from datetime import datetime,timezone

messages = [{'name': 'Aaron', 'date':'2022-06-22 05:07:20.884325+00:00', 'message':'Hey there! Hope you\'re having a pretty okay day.'}]

print(f"Welcome to the messageboard! It is currently {datetime.now(timezone.utc)}.")

name = input("What is your name? ").title()

# check to see if name is Bob, say Bob's not allowed to use this or something
# if str(name).lower = bob:
#   print(f"Bob isn't allowed to use this.\nThis incident will be reported.")

message = input("What is your message? ")

entry = {}
entry['name'] = str(name)
entry['date'] = str(datetime.now(timezone.utc))
entry['message'] = str(message)

messages.append(entry)

print(f"There are {len(messages)} messages.")

for each_message in messages:
    print(f"{each_message['name']} said at {each_message['date']}: {each_message['message']}")

# then just loop back to "What is your name?" - guessing taking this there will involve wrapping the above into a function and then looping that function
# 2.0 should allow the user to actually decide whether to put in a new message or list all currently saved messages
# 3.0 should allow the user to selectively display messages from a certain date (let's just stick to month/day) and/or name
# 4.0 should actually save the messages somewhere and have them persist

# first function will have the welcome message, then ask if the user wants to leave a message or read them (or maybe just exit?)
## will rely on user input, need to anticipate shenanigans
# next function will be the actual message-leaving, then send the user back to the first function
# next function will be the message-listing, then send the user back to the first function
