message_01 = message_02 = message_03 = message_04 = message_05 = messages = ''

def display():
    print('\n' * 50)
    print('01. ' + message_01)
    print('02. ' + message_02)
    print('03. ' + message_03)
    print('04. ' + message_04)
    print('05. ' + message_05)
    if messages == 0: print('>> Leave a message!')
    if messages == 1: print('>> Message box full.')

while message_01 == '':
    display()
    message_01 = input()

while message_02 == '':
    display()
    message_02 = input()

while message_03 == '':
    display()
    message_03 = input()

while message_04 == '':
    display()
    message_04 = input()

while message_05 == '':
    display()
    message_05 = input()
    messages = 1

display()
