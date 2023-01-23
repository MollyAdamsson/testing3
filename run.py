import random 

board_size = 5

# Create the board for the computer and place the ship
computer_board = [[random.choice(["O","S"]) for _ in range(board_size)] for _ in range(board_size)]

# Create the board for the player and place the ship
print("Player's Turn:")
player_board = [[random.choice(["O","S"]) for _ in range(board_size)] for _ in range(board_size)]

# Game loop
while True:
    print("Player's Turn:")
    print_board(player_board)
    print("Computer's Turn:")
    print_board(computer_board)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    if computer_board[guess_row][guess_col] == "S":
        print("Congratulations! You sank the computer's battleship!")
        play_again = input("Do you want to play again? (yes/no)")
        if play_again.lower() == "yes":
            computer_board = [[random.choice(["O","S"]) for _ in range(board_size)] for _ in range(board_size)]
            player_board = [[random.choice(["O","S"]) for _ in range(board_size)] for _ in range(board_size)]
        else:
            print("Thanks for playing!")
            exit()
    else:
        player_board[guess_row][guess_col] = "X"
        print("Player missed the computer's battleship!")
    computer_guess_row = random.randint(0, board_size-1)
    computer_guess_col = random.randint(0, board_size-1)
    if player_board[computer_guess_row][computer_guess_col] == "S":
        print("The computer sank your battleship!")
        play_again = input("Do you want to play again? (yes/no)")
        if play_again.lower() == "yes":
            computer_board = [[random.choice(["O","S"]) for _ in range(board_size)] for _ in range(board_size)]
            player_board = [[random.choice(["O","S"]) for _ in range(board_size)] for _ in range(board_size)]
        else:
            print("Thanks for playing!")
            exit()
    else:
        computer_board[computer_guess_row][computer_guess_col] = "X"
        print("computer missed the player's battleship!")

def print_board(board):
    for row in board:
        print(" ".join(row))