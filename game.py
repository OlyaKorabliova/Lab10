import sys
from btree import BTree
from bt_node import BTNode
from board import Board

def game():
    """
    The game starts here.
    """
    board = Board()
    board_checks = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2)}
    s = ''
    print("\nGame Board:")
    for i in range(1, 10):
        if i % 3 != 0:
            s += str(i) + ' '
        else:
            s += str(i) + '\n'
    print(s)
    for count in range(9):
        k = int(input("Enter your move: "))
        while board.set_value(board_checks[k], 1) is None:
            k = int(input("\tCell isn't empty!\n\tEnter your move again: "))
        print("\tYou've made a move:")
        print(board)
        if board.has_winner() == 1:
            print("\n\tCongratulations! You win! :)\n")
            print(board)
            return new_game()
        print("\tComputer has made a move:")
        board1 = BTNode(board)
        bnt = BTree(board1)
        bnt.expand()
        board = bnt.get_best_move()
        print(board)
        if board.has_winner() == -1:
            print("\n\tUnfortunately, you lose :(\n")
            print(board)
            return new_game()
        if board.still_have_move() == False:
            print("It is a draw.")
            return board

def new_game():
    k = input("\nDo you want to play again? (yes/no): ")
    yes = ['y', 'yes', 'ye']
    no = ['n', 'no']
    if k.lower() in yes:
        game()
    if k.lower() in no:
        print("Good Bye! ;)")
        sys.exit()

game()
