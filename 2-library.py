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
    """Displays options for the user as a menu. Also takes IDs as input to check items in or out (not yet implemented)."""
    while True:
        mm_choice = input("""
Welcome to the library! What would you like to do? You can also enter an item ID to check an item in or out.
    1: Check inventory (limited functionality)
    2: Add an item (not yet implemented)
    3: Remove an item (not yet implemented)
    4: Quit
>> """)
        if mm_choice in {"1","check","list"}:
            list_inventory()
        elif mm_choice in {"2","add"}:
            add_item()
        elif mm_choice in {"3","rm","remove"}:
            remove_item()
        elif mm_choice in {"4","quit","exit"}:
            print("Thanks for visiting the library. Goodbye!")
            quit()
        else:
            check_in_out(mm_choice)

# todo: ask user whether they'd like to list items by medium / year / author, give choices 0/1/2/etc
def list_inventory():
    """Allows the user to display registered inventory."""
    print("You selected 1: Check inventory.")
#    li_choice = input("""
#Would you like to list inventory by:
#    1: Title
#    2: Author
#    3: Year
#    4: Medium
#    5: ID
#    6: Availability
#""")
    for item in inventory:
        print(f"ID {item['id']} - {item['title']} ({item['year']}) by {item['author']}. Medium: {item['medium']}. Available quantity: {item['qty']}")

# todo: implement - take item and query dictionary for values
def check_in_out(item):
    """Allows user to determine whether they're checking an item in or out (after checking to see if both are logical)"""
    if item in inventory:
        if item['qty'] >= 1:
            cio_choice_avail = input(f"You have selected {item['name']}, which currently has {item['qty'].upper()} copies available. Would you like to check a copy in or out? (Enter \"in\" or \"out\".) >> ")
            if cio_choice_avail in {'in','checkin','return'}:
                check_in(item)
            elif cio_choice_avail in {'out','checkout','borrow'}:
                check_out(item)
            else:
                print("Invalid entry. Returning to main menu.")
        else:
            cio_choice_unavail = input(f"You have selected {item['name']}, which currently has {item['qty'].upper()} copies available. Would you like to check a copy in? (Enter \"yes\" or \"no\".) >> ")
            if cio_choice_unavail in {'y','yes'}:
                check_in(item)
            elif cio_choice_unavail in {'n','no'}:
                print("Returning to main menu.")
            else:
                print("Invalid entry. Returning to main menu.")
    else:
        print("Item ID not found / entry did not correspond to an available option. Please make another selection.")

def check_out(item):
    """Subtracts one from the quantity of item."""
    co_choice = input(f"You have selected {item['name']}, which is currently AVAILABLE. Would you like to check it out? (y/n) >> ")
    if co_choice in {'y','yes','yep','ok','sure'}:
        item['qty'] --1
        print(f"You have checked out {item['name']} ({item['id']}). Enjoy!")
        print(f"There are now {item['qty']} of this item available.")
    else:
        print(f"{item['name']} ({item['id']}) was NOT checked out. Returning to main menu.")

# todo: implement - identify item
def check_in(item):
    """Adds one to the quantity of item."""
    ci_choice = input(f"You have selected  {item['name']}, which is currently UNAVAILABLE. Would you like to return a copy?") 
    if ci_choice in {'y','yes','yep','ok','sure'}:
        item['qty'] ++1
        print(f"You have checked in {item['name']} ({item['id']}). Thank you!")
        print(f"There are now {item['qty']} of this item available.")

# todo: make sure year is a number
def add_item():
    """Allows user to add an item to the inventory."""
    item['title'] = input("What is the new item's title? ")
    item['author'] = input(f"Who is {item['title']}'s author? ")
    item['year'] = input(f"In what year was {item['title']} published? ")
    item['medium'] = input(f"What medium is {item['title']} in? ")
    item['id'] = input(f"Enter an ID number for {item['title']}. ")
    item['qty'] = 'available'
    inventory.append(item)

# todo: implement - should require user to enter id and ask for confirmation eg 'Are you sure you want to remove text "Speaker for the Dead" by "Orson Scott Card" (1986)?'
def remove_item(item):
    """Allows user to remove an item from the inventory."""
    choice = input(f"Removing ????")

main_menu()
