from random import randint

# Creating the player and computer's boards
Hidden_Pattern=[[' ']*8 for x in range(8)]
Guess_Pattern=[[' ']*8 for x in range(8)]
Computer_Hidden_Pattern=[[' ']*8 for x in range(8)]
Computer_Guess_Pattern=[[' ']*8 for x in range(8)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1

def get_ship_location():
    #Enter the row number between 1 to 8
    row=input('Please enter a ship row 1-8 ').upper()
    while row not in '12345678':
        print("Please enter a valid row ")
        row=input('Please enter a ship row 1-8 ')
    #Enter the Ship column from A TO H
    column=input('Please enter a ship column A-H ').upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column ")
        column=input('Please enter a ship column A-H ')
    return int(row)-1,let_to_num[column]

#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='X':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = 'X'

# Creating the ships for the computer
create_ships(Computer_Hidden_Pattern)

def count_hit_ships(board):
    count=0
    for row in board:
        for column in row:
            if column=='X':
                count+=1
    return count

# Creating ships for the player
create_ships(Hidden_Pattern)

turns = 10
while turns > 0:
    print('Welcome to Battleship')
    print_board(Guess_Pattern)
    row,column =get_ship_location()
    if Guess_Pattern[row][column] == '-':
        print(' You already guessed that ')
    elif Computer_Hidden_Pattern[row][column] =='X':
        print(' Congratulations you have hit the battleship ')
        Guess_Pattern[row][column] = 'X'
        turns -= 1
    else:
        print('Sorry,You missed')
        Guess_Pattern[row][column] = '-'
        turns -= 1
        if  count_hit_ships(Guess_Pattern) == 5:
        print('Congratulations you have sunk all the battleships')
        break
    print(' You have ' +str(turns) + ' turns remaining ')
    if turns == 0:
        print('Game Over ')
        break

    # Computer's turn
    print("\nComputer's turn")
    comp_row, comp_col = randint(0, 7), randint(0, 7)
    if Computer_Guess_Pattern[comp_row][comp_col] == '-':
        print("Computer already guessed that")
    elif Hidden_Pattern[comp_row][comp_col] == 'X':
        print("Computer hit the battleship")
        Computer_Guess_Pattern[comp_row][comp_col] = 'X'
    else:
        print("Computer missed")
        Computer_Guess_Pattern[comp_row][comp_col] = '-'
    if count_hit_ships(Computer_Guess_Pattern) == 5:
        print("Computer has sunk all the battleships")
        break