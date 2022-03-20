import random


def print_board(board):
    for row in range(3):
        print(board[1 + row*3], "|", board[2 + row*3], "|", board[3 + row*3],)
        #print("  | | ")
        if row < 2:
            print(" -  -  - ")


def initialize_first_player():
    first_player = random.randint(0, 1)
    name_dict = {0: 'computer',
                 1: 'user'}
    print("Begin: \t\t", name_dict[first_player])
    return first_player

current_player = None
user_mark = None
def generate_user_mark():
    user_mark = random.randint(0, 1)
    name_dict = {0: 'cross',
                 1: 'circle'}
    user_mark = name_dict[user_mark]
    print('User mark:\t', user_mark)
    return user_mark
    


current_player = initialize_first_player()
user_mark = generate_user_mark()

board = {}
for x in range(1, 10):
    board[x] = "-"

print(board)
print_board(board)


