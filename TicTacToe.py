# Tic Tac Toe by Jarett Dewbury
import random


# Display Board
def display_board(p1, p2, board, s1, s2):
    print('\n' * 5)
    print(f'player 1 ({p1}) score: {s1}')
    print(f'player 2 ({p2}) score: {s2} \n')

    print("{} | {} | {}".format(board[0], board[1], board[2]))
    print("{} | {} | {}".format(board[3], board[4], board[5]))
    print("{} | {} | {}".format(board[6], board[7], board[8]))


# Gather input from Player
def player_input():
    valid_input = True

    while valid_input:

        player1 = input("Player 1, please pick a marker 'X' or 'O': ")

        if player1 == 'X' or player1 == 'O':

            if player1 == 'X':
                player2 = 'O'
            else:
                player2 = 'X'

            valid_input = False

        else:
            print('\n' * 10)
            print("INVALID INPUT: Please pick a marker 'X' or 'O'! ")

    return player1, player2


# Place marker at position
def place_marker(board, marker, position):
    board[position - 1] = marker
    return board


# Check for winning player
def win_check(board, mark):
    # Horizontal Wins
    if board[0] == mark and board[0] == board[1] and board[0] == board[2]:
        return True
    elif board[3] == mark and board[3] == board[4] and board[3] == board[5]:
        return True
    elif board[6] == mark and board[6] == board[7] and board[6] == board[8]:
        return True

    # Vertical Wins
    elif board[0] == mark and board[0] == board[3] and board[0] == board[6]:
        return True
    elif board[1] == mark and board[1] == board[4] and board[1] == board[7]:
        return True
    elif board[2] == mark and board[2] == board[5] and board[2] == board[8]:
        return True

    # Diagonal Wins
    elif board[0] == mark and board[0] == board[4] and board[0] == board[8]:
        return True
    elif board[2] == mark and board[2] == board[4] and board[2] == board[6]:
        return True

    else:
        return False


# Check for valid move
def space_check(board, position):
    if board[position - 1] == test_board[position - 1]:
        return True
    else:
        return False


# Check for a full board
def full_board_check(board):
    count = 0
    for i in range(0, 9):
        if board[i] == "X" or board[i] == "O":
            count = count + 1
    if count == 9:
        return True
    return False


def replay():
    replay_game = input("Would you like to play again? Type 'Yes' to play again: ")
    if replay_game == "Yes":
        return True
    return False


def valid_choice(choice):
    if choice in range(1, 10):
        return True
    return False


# ________________________________________________________________________________________

print('Welcome to Tic Tac Toe!')

play_game = True
game_on = True
game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
test_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
p1_score = 0
p2_score = 0

# Ask for players input
player1, player2 = player_input()

while play_game:

    # display board
    display_board(player1, player2, game_board, p1_score, p2_score)

    while game_on:

        if full_board_check(game_board):
            print('BOARD IS FULL. NO WINNER!')
            break

        valid_move = False

        while not valid_move:
            move = int(input("Player 1 please select your move: "))
            if valid_choice(move):
                if space_check(game_board, move):
                    game_board = place_marker(game_board, player1, move)
                    display_board(player1, player2, game_board, p1_score, p2_score)
                    valid_move = True
                else:
                    print("INVALID MOVE. TRY AGAIN \n ")

        valid_move = False

        if win_check(game_board, player1):
            print(f'{player1} has won the game!')
            p1_score = p1_score + 1
            break

        if full_board_check(game_board):
            print('BOARD IS FULL. NO WINNER!')
            break

        while not valid_move:
            move = int(input("Player 2 please select your move: "))
            if valid_choice(move):
                if space_check(game_board, move):
                    game_board = place_marker(game_board, player2, move)
                    display_board(player1, player2, game_board, p1_score, p2_score)
                    valid_move = True
                else:
                    print("INVALID MOVE. TRY AGAIN \n ")

        if win_check(game_board, player2):
            print(f'{player2} has won the game!')
            p2_score = p2_score + 1
            break

    if not replay():
        print('\nThanks for playing!')
        break
    else:
        game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        game_on = True
