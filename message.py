from time import strftime

board = []

while True:
    print('\n' * 50)
    for posts in board: # range(len(board))?
        print(posts)
    print('------')
    print('Leave a new message!')
    posts = input() + ' - ' + strftime("%Y-%m-%d %H:%M:%S")
    board = board + [posts]
