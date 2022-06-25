# checking items out of a library!

inventory = [
        {
            'title': 'Ulysses',
            'author': 'James Joyce',
            'year': 1922,
            'medium': 'text',
            'id': '1840226358',
            'qty': 1,
        },
        {
            'title': 'A Portrait of the Artist as a Young Man',
            'author': 'James Joyce',
            'year': 1916,
            'medium': 'text',
            'id': '0679739890',
            'qty': 2,
        },
        {
            'title': 'Dune',
            'author': 'Frank Herbert',
            'year': 1965,
            'medium': 'text',
            'id': '0441172717',
            'qty': 2,
        },
        {
            'title': 'Speaker for the Dead',
            'author': 'Orson Scott Card',
            'year': 1986,
            'medium': 'text',
            'id': '1663634483',
            'qty': 1,
        },
        {
            'title': 'A People\'s History of the United States',
            'author': 'Howard Zinn',
            'year': 1980,
            'medium': 'text',
            'id': '0060838655',
            'qty': 2,
        },
        {
            'title': 'Cloud Atlas',
            'author': 'David Mitchell',
            'year': 2004,
            'medium': 'text',
            'id': '0375507256',
            'qty': 1,
        },
        {
            'title': 'Cloud Atlas',
            'author': ['Lana Wachowski', 'Lilly Wachowski', 'Tom Tykwer'],
            'year': 2012,
            'medium': 'video',
            'id': '2012CA',
            'qty': 1,
        },
        {
            'title': 'Palette',
            'author': 'IU',
            'year': 2017,
            'medium': 'audio',
            'id': '2017PAL',
            'qty': 1,
        },
        {
            'title': 'Strange Desire',
            'author': 'Bleachers',
            'year': 2014,
            'medium': 'audio',
            'id': '2014SD',
            'qty': 0,
        },
        {
            'title': 'The Good Place',
            'author': 'Michael Schur',
            'year': 2020,
            'medium': 'video',
            'id': '2020GP',
            'qty': 1,
        },
]

# everything below this (and probably above this) is WIP.

def main_menu():
    while True:
        mm_choice = input("""
Welcome to the library! What would you like to do? You can also enter an item ID to check an item in or out.
    1: Check inventory
    2: Add an item
    3: Remove an item
    4: Quit
>> """)
        if mm_choice in {"1","check","list"}:
            list_inventory()
        elif mm_choice in {"2","add"}:
            add_item()
        elif mm_choice in {"3","rm","remove"}:
            remove_item()
        elif mm_choice in {"4","quit","exit"}:
            print("Thanks for visiting the library. Good-bye!")
            quit()
        else:
            check_in_out(mm_choice)

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

# check in/out could probably be made into one function, actually
def check_in_out(item):
    cio_choice = input(f"You have selected {item['name']}, which is currently {item['qty'].upper()}. Would you like to check it out? (y/n) >> ")

# todo: implement - identify item
def check_out(item):
    co_choice = input(f"You have selected {item['name']}, which is currently AVAILABLE. Would you like to check it out? (y/n) >> ")
    if co_choice == 'y' OR 'yes' OR 'yep' OR 'ok' OR 'sure':
        item['qty'] = 'unavailable'
        print(f"You have checked out {item['name']} ({item['id']}). Enjoy!")
    else:
        print(f"{item['name']} ({item['id']}) was NOT checked out. Returning to main menu.")

# todo: implement - identify item
def check_in(item):
    ci_choice = input(f"You have selected  {item['name']}, which is currently UNAVAILABLE. Would you like to 
    item['qty'] = 'available'
    print(f"You have checked out {item['name']} ({item['id']}). Thank you!")

# todo: make sure year is a number
def add_item():
    item['title'] = input("What is the new item's title? ")
    item['author'] = input(f"Who is {item['title']}'s author? ")
    item['year'] = input(f"In what year was {item['title']} published? ")
    item['medium'] = input(f"What medium is {item['title']} in? ")
    item['id'] = input(f"Enter an ID number for {item['title']}. ")
    item['qty'] = 'available'
    inventory.append(item)

# todo: implement - should require user to enter id and ask for confirmation eg 'Are you sure you want to remove text "Speaker for the Dead" by "Orson Scott Card" (1986)?'
def remove_item(item):
    choice = input(f"Removing ????")

