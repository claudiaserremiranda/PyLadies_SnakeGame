from random import *

# to define grid size
grid_rows_size = 15
grid_columns_size = 15


def make_grid(grid_rows_size, grid_columns_size):
    """ This function makes a table/grid, which is a list of lists, with dots as entries.
    The grid size is entered as arguments (rows , columns)."""    
    table = []
    for j in range (grid_rows_size):
        row = []
        for i in range (grid_columns_size):
            row.append(".")
        table.append(row)
    return table    

def print_grid(table):
    """This function prints a list of lists in a table format."""
    for row in table:
        for dot in row:
            print(dot, end=" ")
        print ()    

def draw_map (snake_body, snake_food):
    """ This function gets a list of coordinates (snake body and snake food) as arguments.
    Each coordinate is composed by pairs (tuples) of numbers smaller than the grid size, which specify 
    the row and column of a grid, and outputs them as a map. The coordinates that are in the snake_body list 
    are drawn as 'X' and the coordinates that are in the snake_food list are drawn as '0'.
    First number in the pair represent the rows in the grid and the second number in the pair represents columns."""
   
    map = make_grid(grid_rows_size, grid_columns_size)
    
    for coordinate in snake_body:               #the snake body is represented by 'X'
        row = coordinate[0]
        column = coordinate[1]
        map[row][column] = "X"
    
    for coordinate in snake_food:                #the snake food is represented by 'O'
        row = coordinate[0]
        column = coordinate[1]
        map[row][column] = "O"    
        return map

# defines length and initial position of the snake
snake_body = [(int(grid_rows_size/3),int(grid_columns_size/3))]
# defines the initial position of the snake food      
snake_food = [(int(grid_rows_size/2),int(grid_columns_size/2))]   

def snake_movement (snake_body, direction):
    """This function gets the coordinates of the snake body as a list and the direction keyword ('w'=up,'s'=down,
    'd'=right,'a'=left) and adds the new coordinate to the list.
    If the new coordinate does not correspond to a snake food coordinate (snake not eating food), then the function
    deletes the first coordinate in the previous existing list, meaning the list will have the same length as the initial one. 
    This means the snake is only moving, not growing.
    If the snake eats the food, then the snake moves and grows (new coordinate added and none deleted)."""
    
    if direction == "w":
        new_row = snake_body[-1][0] - 1
        new_column = snake_body[-1][1]
        
        if new_row < 0 or new_row > grid_rows_size - 1:         #raises an error if new coordinates are out of the map
            raise ValueError
        if (new_row,new_column) in snake_body:  #raises an error if the new coordinate is already in the list,
            raise ValueError                    #meaning the snake will 'eat' the own tail.   
        
        snake_body.append((new_row, new_column))
        if not any(item in snake_body for item in snake_food):   #checks if any coordinate of the snake_food is not in coordinates of snake_body
            del snake_body[0]                                    #snake moving and not growing
    
    
    elif direction == "s":                              # same comments as above
        new_row = snake_body[-1][0] + 1
        new_column = snake_body[-1][1]    
        
        if new_row < 0 or new_row > grid_rows_size - 1:                  
            raise ValueError
        if (new_row,new_column) in snake_body:        
            raise ValueError                            
        
        snake_body.append((new_row, new_column))
        if not any(item in snake_body for item in snake_food):
            del snake_body[0]

    elif direction == "a":                              # same comments as above
        new_row = snake_body[-1][0]
        new_column = snake_body[-1][1] - 1
        
        if new_column < 0 or new_column > grid_columns_size - 1:            
            raise ValueError                            
        if (new_row,new_column) in snake_body:         
            raise ValueError                            
        
        snake_body.append((new_row, new_column))
        if not any(item in snake_body for item in snake_food):
            del snake_body[0]

    elif direction == "d":                              # same comments as above
        new_row = snake_body[-1][0]
        new_column = snake_body[-1][1] + 1
        
        if new_column < 0 or new_column > grid_columns_size - 1:            
            raise ValueError
        if (new_row,new_column) in snake_body:         
            raise ValueError                            
        
        snake_body.append((new_row, new_column))
        if not any(item in snake_body for item in snake_food):
            del snake_body[0]


def play_snake():
    """This function asks the user for the movement direction ('w'=up,'s'=down,'d'=right,'a'=left) and draws a map,
    making the snake move (and grow if eating the food). Entering 'end' stops the game. Each food is eaten by the
    snake increases your score by 1."""
    score = 0
    while True:
        print ("SCORE = ", score)
        direction = input("direction: ")

        if direction == "end":
            print ("The game was terminated!")
            break
       
        try:
            snake_movement(snake_body, direction)    #updates the coordinates list based on user input
        except ValueError:                           #Game over if snake moves out of the map or 'eats' own tail
            print ("Game over")
            break        

        #checks if any coordinate of the snake_food is in snake_body list, which means the snake has eaten the food.
        #a new random snake food coordinate is generated
        if any(item in snake_body for item in snake_food):
            score += 1
            while True:
                new_snake_food_row = randrange(grid_rows_size - 1)              
                new_snake_food_column = randrange(grid_columns_size - 1) 
                new_snake_food = (new_snake_food_row, new_snake_food_column)
                if (new_snake_food) not in snake_body:     #to ensure new snake food position is not part of snake body
                    snake_food.append(new_snake_food)
                    del snake_food[0]                   #only one snake food available at a time/delets previous coordinate
                    break

        map = draw_map(snake_body, snake_food)
        print_grid(map)


# start playing the game
play_snake()
