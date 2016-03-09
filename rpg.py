import sys, random

location = 'home'
response = home_window = home_book = home_pews = 0

if response == 'exit':
    sys.exit()

def choice():
    print('What do you want to do? Type CHECK for options.')
    response = input()

def home():
    if home_window == 0:
        print('There is a stained-glass WINDOW you can look out of.')
    if home_book == 0:
        print('There is a BOOK on a seat in front of the ALTAR.')
    if home_pews == 0:
        print('There are thirteen rows of dilapidated PEWS.')
    choice()

def check():
    if location == 'home':
        home()
    if location == 'cemetary':
        cemetary()
    if location == 'forest':
        forest()
    if location == 'cave':
        cave()

if response == 'CHECK':
       check()

while True:
    print('You wake up in a dusty church.')
    choice()

if location == 'home' and response == 'WINDOW':
    print('You peer out the stained-glass window. You see red, blue, and pink.')
    print('It\'s dark outside.')
    choice()

if location == 'home' and response == 'BOOK':
    print('You cross into the chancel and pick up the abandoned HYMNAL.')
    print('It contains various songs, chants, and hymns designed for the faithful.')
    choice()

if response == 'HYMNAL'
    print('A book of songs.)
    choice()

if location == 'home' and response == 'PEWS':
    print('You walk down the aisle into nave and check the seats.')
    print('Nothing.')
    choice()


