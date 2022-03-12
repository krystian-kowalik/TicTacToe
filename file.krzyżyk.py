import random


def print_board():
    for x in range(3):
        print("  | | ")
        if x < 2:
            print(" - - - ")

def initialize_first_player():
    first_player = random.randint(0, 1)
    name_dict = {0: 'computer',
                 1: 'user'}
    print("Begin: ", name_dict[first_player])


initialize_first_player()
print_board()


