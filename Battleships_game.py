  ### THE SHIP IS 1X1 IN SIZE. YOU HAVE 3 ATTEMPTS. GOOD LUCK!###
    ### ### COLUMN AND ROW INDEXING STARTS FROM ZERO ### ###
from random import randint

board = []

# Creating a 5x5 board
for x in range(5):            
    board.append(["O"] * 5)     

# Function to print the board continuously
def print_board(board):       
    for row in board:           
        print(" ".join(row))

print_board(board)

# Functions to generate a random row and column
def random_row(board):
    return randint(0, len(board) - 1)        

def random_col(board):
    return randint(0, len(board[0]) - 1)      

# Generating a random location for the ship
ship_row = random_row(board)            
ship_col = random_col(board) 
print(ship_col)     
print(ship_row)         

# Guessing the ship's location
for turn in range(4):         
    guess_row = int(input("Guess Row: "))       
    guess_col = int(input("Guess Col: "))        

    # Condition for hitting the ship
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")        
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4): 
            print("Oops, that's not even in the ocean.")       # Condition for "hitting" outside the map
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")             # Condition for "hitting" the same spot
        else:
            print("You missed my battleship!")                 # Condition for missing
            board[guess_row][guess_col] = "X"
        print("Turn", turn + 1)
        if turn == 3:                                         # Game over after 4 attempts
            print("Game Over!, computer won!")          
        print_board(board)  
