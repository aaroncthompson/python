from time import strftime
message_01 = message_02 = message_03 = message_04 = message_05 = messages = ''

def display():
    print('\n' * 50)
    print('01. ' + message_01)
    print('02. ' + message_02)
    print('03. ' + message_03)
    print('04. ' + message_04)
    print('05. ' + message_05)
    if message_05 == '':
        print('>> Leave a message!')
    else:
        print('>> Message box full.')

while message_01 == '':
    display()
    message_01 = input() + ' - ' + strftime("%Y-%m-%d %H:%M:%S")

while message_02 == '':
    display()
    message_02 = input() + ' - ' + strftime("%Y-%m-%d %H:%M:%S")

while message_03 == '':
    display()
    message_03 = input() + ' - ' + strftime("%Y-%m-%d %H:%M:%S")

while message_04 == '':
    display()
    message_04 = input() + ' - ' + strftime("%Y-%m-%d %H:%M:%S")

while message_05 == '':
    display()
    message_05 = input() + ' - ' + strftime("%Y-%m-%d %H:%M:%S")
    messages = 1

display()
