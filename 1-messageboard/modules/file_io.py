import json
import message_bank as mb

def load_file():
    """Attempts to load messageboard with default name, otherwise starts us off with a default message."""
    try:
        with open('messageboard.json') as messageboard_file:
            mb.messages = json.load(messageboard_file)
    except FileNotFoundError:
        mb.messages = [{'name': 'Aaron', 'date':'2022-06-22 05:07:20.884325+00:00', 'message':'Hey there! Hope you\'re having a pretty okay day.'}]

# is there any benefit to appending new messages over just overwriting old+new? still have to load old to show them so it doesn't seem like we'd be saving memory.
def write_file(updated_messages):
    """Appends new messages to messageboard."""
    with open('messageboard.json', 'w') as messageboard_file:
        json.dump(updated_messages, messageboard_file)
