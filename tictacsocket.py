import pygame
import sys

# Window
WIDTH = 300
HEIGHT = 325

# Game Settings
PlayerTurn = "X" # Makes X start first by default, will get changed to decide whos turn it is
PlayerX = 1 # Gives them id's to use
PlayerO = 0 # Gives them id's to use

# Creates our board layout to put values to. by default, the board is blank.
grid = [[None, None, None], [None, None, None], [None, None, None]]
winner = None # Adds a winner variable for later

# ttt is a properly initalised pyGame display variable
# Go back to line 72 and understand it
# Line 149 is probably the best area to implement a moving counter because it is where the player turn is changed.
# I'm not sure whether I need to make grid a global variable. The function doesn't need to change grid...doesn't it?
# Consider adding a move counter

def initialiseBoard(ttt):
    # Job: Initialise the board and return the board as a variable

    white = (250, 250, 250)

    # Setup background surface
    background = pygame.Surface(ttt.get_size()) # Creates a surface object with the window size
    background = background.convert() # Converts toe background to pixel format
    background.fill(white) # Converts the backgorund to a white color (I think)

    # Draw Grid Lines

    # Vertical lines
    pygame.draw.line(background, (0, 0, 0), (100, 0), (100, 300), 2)
    pygame.draw.line(background, (0, 0, 0), (200, 0), (200, 300), 2)

    # horizontal lines...
    pygame.draw.line(background, (0, 0, 0), (0, 100), (300, 100), 2)
    pygame.draw.line(background, (0, 0, 0), (0, 200), (300, 200), 2)

    # Note about lines: Draws the lines with the Surface, Color, Start pos, End pos, and width

    return background # returns the fully realised background

def checkforFull():
    for row in grid: # For every row in grid (keeping in mind grid is just made up of 3 lists)
        if None in row: # If there is None in any of the lists in grid
            finished = False # The game hasn't finished yet
            break
        else: # If there isn't...
            finished = True # The game has finished
    return finished

def drawStatus(board):
    # Job: Shows status at the bottom of the board (i.e player turn, num of moves, etc)
    # In this case, board is the initialised game board where the status will be drawn onto

    black = (10, 10, 10)
    white = (250, 250, 250)

    global PlayerTurn, winner, grid

    # Determine what to write
    if winner == None and checkforFull() == False: # If there isn't a winner and the board isn't full
        message = "{}'s turn".format(PlayerTurn) # make message equal to whoevers turn it is
    elif winner != None:
        message = "{} Wins!".format(winner) # Otherwise, display whoever wins instead
    elif winner == None and checkforFull() == True: # If there isn't a winner and the board is full
        message = "A tie!" # Call for a tie

    # Setup (render) the message
    font = pygame.font.Font(None, 24) # Creates a default pygame font with the size of the font in pixels
    text = font.render(message, True, (black)) # Creates a new surface with the specified message on it.
    # It doesn't allow you to add to an existing surface, so we'll have to blit this surface onto our one.
    # After that, we set antialiasing to true. It then sets the color of the text to black.

    # Send the finished status onto the board
    board.fill(white, (0, 300, 300, 25))
    board.blit(text, (10, 300)) # Pastes the status onto the board at the coordinates 10, 300

def showBoard(ttt, board):
    # Job: Redraw the board onto the display (basically updates the screen)
    # In this case, ttt is the initialized pyGame display and board is the game board surface

    drawStatus(board) # Draw/redraws the status info at the bottom of the board
    ttt.blit(board, (0, 0)) # Places the board onto the display at the very base coordinates (top left corner)
    pygame.display.flip() # Updates the entire display

def boardPosition(mouseX, mouseY):
    # Job: Find out which board space (i.e row, column) the user clicked in based on their mouse coordinates
    # Here, mouseX is the X coordinate the user clicked and mouseY is the Y coordinate the user clicked

    # Note: Lists are 0 based in terms of index. This means that if you call for the 0th item (i.e list[0]), you will
    # get the first, as the index "starts" from 0.

    # Find the row the user clicked in
    if mouseY < 100: # If mouseY is less than 100
        row = 0 # It clicked in the 1st row
    elif mouseY < 200: # If mouseY is less than 200
        row = 1 # It clicked in the 2nd row
    else: # Otherwise
        row = 2 # It clicked in the 3rd row

    # Find the column the user clicked in
    if mouseX < 100: # If mouseX is less than 100
        col = 0 # It clicked in the 1st row
    elif mouseX < 200: # If mouseX is less than 200
        col = 1 # It clicked in the 2nd row
    else: # Otherwise
        col = 2 # It clicked in the 3rd row

    return (row, col) # Returns the tuple containing the row and column that the user clicked in

def drawMove(board, boardRow, boardCol, Symbol):
    # Job: Draw either an X or an O (Symbol) on the board in a specific boardRow and boardCol
    # Board is the game board surface we are drawing on. boardRow and boardCol are the row and column in which
    # we will draw the symbol in. Symbol is either an X or an O, based on who's turn it is.

    # Note: Lists are 0 based in terms of index. This means that if you call for the 0th item (i.e list[0]), you will
    # get the first, as the index "starts" from 0.

    # Finds the center of the box we will draw in
    centerX = ((boardCol) * 100) + 50
    centerY = ((boardRow) * 100) + 50

    # Draws the appropriate symbol
    if (Symbol == "O"): # If the Symbol is O, draw a circle in the specified square
        pygame.draw.circle(board, (0, 0, 0), (centerX, centerY), 44, 2)
    elif Symbol == "X": # If the Symbol is X, draw two lines (i.e an X) in the specified square
        pygame.draw.line(board, (0, 0, 0), (centerX - 22, centerY - 22), (centerX + 22, centerY + 22), 2)
        pygame.draw.line(board, (0, 0, 0), (centerX + 22, centerY - 22), (centerX - 22, centerY + 22), 2)

    # Mark the square as occupied
    grid[boardRow][boardCol] = Symbol

def clickBoard(board):
    # Job: Find out where the user clicked and if the space isn't occupied, have a symbol drawn there
    # board is the game board surface

    global grid, PlayerTurn # Necessary to find out whether a space is occupied and which symbol to draw

    mouseX, mouseY = pygame.mouse.get_pos() # Makes mouseX and mouseY equal to the coordinates of the mouse
    clickedBox = boardPosition(mouseX, mouseY)
    row = clickedBox[0] # makes row equal to the first part of the tuple returned by boardPosition
    col = clickedBox[1] # makes col equal to the second part of the tuple returned by boardPosition
    # As a note, boardPosition, returns the row and column that the user clicked in

    # Check to see if the space is empty
    if grid[row][col] == "X" or grid[row][col] == "O": # If an X or an O is present in the box that was clicked
        return

    # Draw an X or an O, based on whos turn it is
    drawMove(board, row, col, PlayerTurn)

    # Toggle PlayerTurn to make it the other persons turn
    if PlayerTurn == "X":
        PlayerTurn = "O"
    elif PlayerTurn == "O":
        PlayerTurn = "X"

def gameFinished(board):
    # Job: To check for either a player win or a tie
    # board is the game board surface

    global grid, winner # Needs to be able to change the winner variable if someone has won
    red = (250, 0, 0)
    LINETHICKNESS = 5 # The thickness of the line used to represent 3 in a row
    # For extra info:
    # To draw a line,the following variables are needed (in order)
    # Surface, color, start position, end position, width

    # Check for rows in which someone has won
    for row in range(0, 3): # In any of the rows (i.e row 1, row 2, or row 3)
        # If the 1st, 2nd and 3rd values are the same and are not empty...
        if ((grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None)):
            winner = grid[row][0] # The winner is the symbol on the first value of the row (i.e column 1)
            # Draws a line through the row
            pygame.draw.line(board, (red), (0, (row + 1) * 100 - 50), (300, (row + 1) * 100 - 50), LINETHICKNESS)
            break # Break out of the for loop

    # Check for columns in which someone has won
    for col in range(0, 3): # IN any of the columns (i.e column 1, column 2 or column 3
        # If the 1st, 2nd and 3rd values are the same and are not empty...
        if (grid[0][col] == grid[1][col] == grid[2][col]) and (grid[0][col] is not None):
            winner = grid[0][col] # The winner is the symbol on the first value of the column (i.e row 1)
            # Draws a line through the column
            pygame.draw.line(board, (red), ((col + 1) * 100 - 50, 0), ((col + 1) * 100 - 50, 300), LINETHICKNESS)
            break # Break out of the for loop

    # Check for diagonal wins
    # If the diagonal values starting from the top left are all the same and are not empty
    if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
        winner = grid[0][0] # The winner is the symbol in the top left
        pygame.draw.line(board, (red), (50, 50), (250, 250), LINETHICKNESS) # Draw a line through the diagonal

    # If the diagonal values starting from the top right are all the same and are not empty
    if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
        winner = grid[0][2] # The winner is the symbol in the top right
        pygame.draw.line(board, (250, 0, 0), (250, 50), (50, 250), LINETHICKNESS) # Draw a line through the diagonal

    # Check for ties
    # If the board is full and winner is not equal to X or O
    # It is a tie. Change the status
    drawStatus(board)

def main():
    pygame.init()
    ttt = pygame.display.set_mode((WIDTH, HEIGHT)) # Creates the surface with the given width and height
    pygame.display.set_caption('Tic-Tac-Toe') # Sets the caption for the game
    board = initialiseBoard(ttt) # Initalises the board
    running = True # On/Off switch

    while running == True: # Main event loop
        for event in pygame.event.get(): # Finds the events that are currently queued up
            if event.type == pygame.QUIT: # If the window close button is pressed
                running = False # The game stops running
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # If the mouse button is pressed
                # Find out where the user clicked and if the space isn't occupied, have a symbol drawn there
                clickBoard(board)

        gameFinished(board) # Check to see if the game finished

        showBoard(ttt, board) # Update the display

if __name__ == "__main__":
    main()