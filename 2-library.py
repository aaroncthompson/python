# checking items out of a library!

inventory = [
        {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'year': 1922,
            'medium': 'text',
            'id': '1840226358',
            'availability': 'in',
        },
        {
            'title': 'A Portrait of the Artist as a Young Man',
            'author': 'James Joyce',
            'year': 1916,
            'medium': 'text',
            'id': '0679739890',
            'availability': 'out',
        },
        {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'year': 1965,
            'medium': 'text',
            'id': '0441172717',
            'availability': 'in',
        },
        {
            'title': 'Speaker for the Dead',
            'author': 'Orson Scott Card',
            'year': 1986,
            'medium': 'text',
            'id': '1663634483',
            'availability': 'in',
        },
        {
            'title': 'A People\'s History of the United States',
            'author': 'Howard Zinn',
            'year': 1980,
            'medium': 'text',
            'id': '0060838655',
            'availability': 'in',
        },
        {
            'title': 'Cloud Atlas',
            'author': 'David Mitchell',
            'year': 2004,
            'medium': 'text',
            'id': '0375507256',
            'availability': 'out',
        },
        {
            'title': 'Cloud Atlas',
            'author': ['Lana Wachowski', 'Lilly Wachowski', 'Tom Tykwer'],
            'year': 2012,
            'medium': 'video',
            'id': '2012CA',
            'availability': 'in',
        },
        {
            'title': 'Palette',
            'author': 'IU',
            'year': 2017,
            'medium': 'audio',
            'id': '2017PAL',
            'availability': 'in',
        },
        {
            'title': 'Strange Desire',
            'author': 'Bleachers',
            'year': 2014,
            'medium': 'audio',
            'id': '2014SD',
            'availability': 'in',
        },
        {
            'title': 'The Good Place',
            'author': 'Michael Schur',
            'year': 2020,
            'medium': 'video',
            'id': '2020GP',
            'availability': 'in',
        },
]

def main_menu():
    mm_choice = input("""
Welcome to the library! What would you like to do?
    1: Check inventory
    2: Check out an item
    3: Check in an item
    4: Quit
>> """)

# todo: implement - ask user whether they'd like to list items by medium / year / author, give choices 0/1/2/etc
def list_inventory():
    print("You selected 1: Check inventory.")
    li_choice = input("""
Would you like to list inventory by:
    1: Title
    2: Author
    3: Year
    4: Medium
    5: ID
    6: Availability
""")

def check_out(item):
    if item['availability'] == 'in':
        item['availability'] = 'out'
        print(f"You have checked out {item['name']} ({item['id']}). Enjoy!")
    else:
        print(f"{item['name']} ({item['id']}) is currently not available for checkout.") 

def check_in(item):
    if item['availability'] == 'out':
        item['availability'] = 'in'
        print(f"You have checked out {item['name']} ({item['id']}). Thank you!")
    else:
        print(f"{item['name']} ({item['id']}) is not currently checked out.")

# todo: make sure year is a number
def add_item():
    item['title'] = input("What is the new item's title? ")
    item['author'] = input(f"Who is {item['title']}'s author? ")
    item['year'] = input(f"In what year was {item['title']} published? ")
    item['medium'] = input(f"What medium is {item['title']} in? ")
    item['id'] = input(f"Enter an ID number for {item['title']}. ")
    item['availability'] = 'in'
    inventory.append(item)

# todo: implement - should require user to enter id and ask for confirmation eg 'Are you sure you want to remove text "Speaker for the Dead" by "Orson Scott Card" (1986)?'
def remove_item(item):
    choice = input(f"Removing ????")

