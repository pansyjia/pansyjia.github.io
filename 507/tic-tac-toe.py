import os
import random

board = [" "," "," "," "," "," "," "," "," "]

######### show a board #########
def show_board():
    print(" {} | {} | {} ".format(*board[0:3]))
    print("-----------")
    print(" {} | {} | {} ".format(*board[3:6]))
    print("-----------")
    print(" {} | {} | {} ".format(*board[6:9]))


######### check for wins ########
def check_winner(board,player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player) :
         return True
    else:
         return False


########## check for a tie #######
def check_tie(board):
    if " " in board:
        return False
    else:
        return True


########## get computer move ########
def get_computer_move(board,player):
    random.seed()
    move = random.randint(0,8)
    return move


########## create a loop ########
while True:
    show_board()

# ask the player X to make a move
    move = input("Plese make a move for X by inputing a number between 0-8.")
    move = int(move)

# check if a move is valid
    if board[move]== " ":
        board[move]= 'X'
    else:
        print ("Sorry. This position has been taken. Please try another number between 0-8.")

# check for wins
    if check_winner(board,'X'):
        os.system("clear")
        show_board()
        print("X wins!")
        break

# when a tie happens
    if check_tie(board):
        print("Tie!")
        break


# get O input
    move2 = get_computer_move(board,'O')

# check invalid move
    if board[move2]== " ":
        board[move2]= 'O'
    else:
        print ("Sorry. This position has been taken. Please try another number between 0-8.")

# check for o win
    if check_winner(board,'O'):
        os.system("clear")
        show_board()
        print("O wins!")
        break

# when a tie happens
    if check_tie(board):
        print("Tie!")
        break
