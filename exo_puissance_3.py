def display_grid(grid):
    for line in range(len(grid)):
        result = str(line) + "    "
        
        for column_index in range(len(grid[0])):
            result = result + str((grid[line][column_index])) + "    "
        print(result + "\n")
    
    result = " "
    for column_index in range(len(grid[0])):
        result = result + "    " + str(column_index) 
    print(result)

def play_one_turn(grid, current_player):
    
    display_grid(tableau)
    
    column = int(input("Joueur " + str(current_player) + ": Dans quelle colonne souhaitez-vous placer un jeton ? "))
    
    grid = place_token(grid, current_player, column)

    return check(grid, column)

def place_token(grid, current_player, column):

    line = 0

    while line <= 4 and grid[line][column] == ".":
        line = line + 1

    line = line - 1

    if line >= 0:
        if current_player == 1:
            token = "O"
        else: 
            token = "X"
        grid[line][column] = token

    return grid

def check_vertical(grid, column, line):
    
    if line >= 3:
        return False
    
    token = grid[line][column]

    if grid[line + 1][column] and grid[line + 2][column] == token:
        return True

    return False

def check_horizontal(grid, column, line):
    
    token = grid[line][column]
    
    if column <= 2:
        if grid[line][column + 1] == token and grid[line][column + 2] == token:
            return True
    
    if column >= 2:
        if grid[line][column - 1] == token and grid[line][column - 2] == token:
            return True
    
    if column >= 1 and column <= 3:
        if grid[line][column - 1] == token and grid[line][column + 1] == token:
            return True
    
    return False

def check_diagonal(grid, column, line):

    token = grid[line][column]

    if column <= 2 and line <= 2:
        if grid[line + 1][column + 1] == token and grid[line + 2][column + 2] == token:
            return True
    
    if column >= 2 and line >= 2:
        if grid[line - 1][column - 1] == token and grid[line - 2][column - 2] == token:
            return True
    
    if column >= 1 and column <= 3 and line >= 1 and line <= 3:
        if grid[line - 1][column - 1] == token and grid[line + 1][column + 1] == token:
            return True
    
    if column <= 2 and line >= 2:
        if grid[line - 1][column + 1] == token and grid[line - 2][column + 2] == token:
            return True
    
    if column >= 2 and line <= 2 :
        if grid[line + 1][column - 1] == token and grid[line + 2][column - 2] == token:
            return True

    if column >= 1 and column <= 3 and line >= 1 and line <= 3:
        if grid[line - 1][column + 1] == token and grid[line + 1][column - 1] == token:
            return True

    return False

def check(grid, column):
    line = 0
    while grid[line][column] == ".":
        line = line + 1

    if check_vertical(grid, column, line) == True:
        return True

    if check_horizontal(grid, column, line) == True:
        return True
    
    if check_diagonal(grid, column, line) == True:
        return True
    
    return False

# -- main code -- #
tableau = [
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."],
    [".", ".", ".", ".", "."]
]

winner = None
current_player = 1

while winner == None:
    
    if play_one_turn(tableau, current_player) == True:
        winner = current_player
    #change player
    else:
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1

print("Bravo ! Le joueur " + str(winner) + " a gagné la partie !")
display_grid(tableau)