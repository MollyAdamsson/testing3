from random import randint

player_ships = [[' ']*8 for x in range(8)]
player_guesses = [[' ']*8 for x in range(8)]
computer_ships = [[' ']*8 for x in range(8)]
computer_guesses = [[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_player_guess():
    #Enter the row number between 1 to 8
    row=input('Please enter a guess row 1-8 ').upper()
    while row not in '12345678':
        print("Please enter a valid row ")
        row=input('Please enter a guess row 1-8 ')
    #Enter the Ship column from A TO H
    column=input('Please enter a guess column A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column ")
        column=input('Please enter a guess column A-H ')
    return int(row)-1,let_to_num[column]


#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'

def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

create_ships(player_ships)
create_ships(computer_ships)
turns = 10
while turns > 0:
    print('Player Turn')
    print_board(player_guesses)
    player_row, player_column = get_player_guess()
    if player_guesses[player_row][player_column] == '-':
        print(' You already guessed that ')
    elif computer_ships[player_row][player_column] =='X':
        print(' Player has hit the battleship ')
        player_guesses[player_row][player_column] = 'X'
    else:
        print('Player missed')
        player_guesses[player_row][player_column] = '-'
    if  count_hit_ships(player_guesses) == 5:
        print("Player has sunk all the battleships ")
        break
    print('Player has ' +str(turns) + ' turns remaining ')

    # Computer's turn
    create_ships(player_ships)
    create_ships(computer_ships)
    turns = 10
    while turns > 0:
       print('Computer Turn')
    computer_row, computer_column = randint(0,7), randint(0,7)
    if computer_guesses[computer_row][computer_column] == '-':
        print('Computer already guessed that')
    elif player_ships[computer_row][computer_column] =='X':
        print(' Computer has hit the battleship ')
        computer_guesses[computer_row][computer_column] = 'X'
    else:
        print('Computer missed')
        computer_guesses[computer_row][computer_column] = '-'
    if  count_hit_ships(computer_guesses) == 5:
        print("Computer has sunk all the battleships ")
        break
    turns -= 1
    if turns == 0:
        print('Game Over ')
        break