import pygame
import sys

"""
Plan: Rework my tic tac toe game
1. Move as much of the Board related functions to the class Board
2. Consider making Board, Symbol, and Status part of a bigger class: Draw
3. Maybe make a constants file (look at Battleships by Timbledum
4. Consider battleships as a new game. It would be complicated enough to play multiple rounds without getting board,
we might end up working with sprites for the ships, and it would be fun and challenging.
5. 


"""

WIDTH = 300
HEIGHT = 325
LINETHICKNESS = 5  # The thickness of the line used to represent 3 in a row
RED = (250, 0, 0)
WHITE = (250, 250, 250)
BLACK = (0, 0, 0)
CELL_DIMENSIONS = 100

class Game:
	""" A class to contain the game state, as well as useful methods for modifying it"""

	def __init__(self):
		self.player_turn = "X" # Makes X start first by default

		# Creates our board layout to put values to. by default, the board is blank.
		self.grid = [[None, None, None], [None, None, None], [None, None, None]]
		self.winner = None  # Adds a winner variable for later


	def check_for_full(self):
		for row in self.grid:
			# For every row in grid (keeping in mind grid is just made up of 3 lists)
			if None in row:  # If there is None in any of the lists in grid
				board_full = False  # The game hasn't finished yet
				break
			else:  # If there isn't...
				board_full = True  # The game has finished
		return board_full

	def game_message(self):
		# Determine what to write
		if self.winner == None and self.check_for_full() == False:
			# If there isn't a winner and the board isn't full
			message = "{}'s turn".format(self.player_turn)
		# make message equal to whoevers turn it is
		elif self.winner != None:
			message = "{} Wins!".format(self.winner)
		# Otherwise, display whoever wins instead
		elif self.winner == None and self.check_for_full() == True:
			# If there isn't a winner and the board is full
			message = "A tie!"  # Call for a tie
		return message

	def game_won(self):
		""" A method to check for either a player win or a tie
			board = the game board surface

			Extra info: To draw a line,the following variables are needed (in order) Surface, color, start position, end position, width """

		grid = self.grid

		# Check for rows in which someone has won
		for row in range(0, 3):  # In any of the rows (i.e row 1, row 2, or row 3)
			# If the 1st, 2nd and 3rd values are the same and are not empty...
			if (grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None):
				self.winner = grid[row][0] # The winner is the symbol on the first value of the row (i.e column 1)\
				return ("row", row)  # Break out of the for loop

		# Check for columns in which someone has won
		for col in range(0, 3):  # In any of the columns (i.e column 1, column 2 or column 3 i
			# f the 1st, 2nd and 3rd values are the same and are not empty...
			if (grid[0][col] == grid[1][col] == grid[2][col]) and (grid[0][col] is not None):
				self.winner = grid[0][col] # The winner is the symbol on the first value of the column (i.e row 1)
				return ("column", col)  # Break out of the for loop

		# Check for diagonal wins
		# If the diagonal values starting from the top left are all the same and are not empty
		if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
			self.winner = grid[0][0]  # The winner is the symbol in the top left
			return ("diag1", None)  # Draw a line through the diagonal

		# If the diagonal values starting from the top right are all the same and are not empty
		if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
			self.winner = grid[0][2]  # The winner is the symbol in the top right
			return ("diag2", None)  # Draw a line through the diagonal

		else:
			# Check for ties
			# If the board is full and winner is not equal to X or O
			# It is a tie. Change the status
			return (None, None)


	def cell_full(self, row, col):
		""" Checks to see if the board is full by looking to see if there is a None value in any of the cells"""
		cell = self.grid[row][col]
		return cell != None # Returns True or False

	def toggle_turn(self):
		"""Turn the player turn to the opposite player."""
		if self.player_turn == "X":
			self.player_turn = "O"
		elif self.player_turn == "O":
			self.player_turn = "X"

class App:
	""" A class responsible for initialising the game, taking inputs, and displaying the board and symbols"""

	def __init__(self):
		pygame.init() # Initialises pygame
		self.ttt = pygame.display.set_mode((WIDTH, HEIGHT)) # Creates the surface with the given width and height
		pygame.display.set_caption("Tic Tac Toe") # Sets the caption for the game
		self.board = self.Draw.Board.initialise_board(self) # Initalises the board
		self.game = Game() # Gives the App class access to the Game class
		self.play_game() # Runs the play_game method
		self.winner = None


	@staticmethod
	def board_position(mouseX, mouseY):
		""" Responsible for finding out which board space (i.e row, column) the user clicked in
		based on their mouse coordinates. Here, mouseX is the X coordinate the user clicked in and mouseY is the Y coordinate"""

		point = mouseY // CELL_DIMENSIONS, mouseX // CELL_DIMENSIONS
		return point # Note: The reason I put mouseY first is that mouseX is the horizontal axis, i.e which column
					 # While mouseY is the vertical axis, i.e which row.

	def click_board(self):
		"""Job: Find out where the user clicked and if the space isn't occupied,
		have a symbol drawn there board is the game board surface."""

		mouseX, mouseY = pygame.mouse.get_pos() # Makes mouseX and mouseY equal to the coordinates of the mouse

		row, col = self.board_position(mouseX, mouseY) # board_position returns which row and column the user clicked in

		if self.game.cell_full(row, col): # If an X or an O is present in the box that was clicked
			return

		# Draw an X or an O, based on whos turn it is
		self.Draw.Symbols.draw_move(self, row, col)

		# Toggle PlayerTurn to make it the other persons turn
		self.game.toggle_turn()

	def play_game(self):
		"""The main game loop"""
		running = True # On/Off switch
		win = False

		while running == True: # The main event loop
			for event in pygame.event.get():
				# Finds the events that are currently queued up
				if event.type == pygame.QUIT:  # If the window close button is pressed
					running = False  # The game stops running
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					# If the mouse button is pressed
					# Find out where the user clicked and if the space isn't occupied, have a symbol drawn there
					self.click_board()

			if winner == "X" or winner == "O":
				win = True

			self.Draw.Symbols.display_winning(self)  # Check to see if the game finished
			self.show_board()  # Update the display
			self.Draw.Status.draw_status(self) # Updates the status
			if win == True:
				running = False

	def show_board(self): # My reasoning for not putting this under draw is that its purpose is to update the screen
		""" Redraws the board onto the display (basically updates the screen)
			In this case, ttt is the initialized pyGame display and board is the game board surface."""

		# Draw/redraws the status info at the bottom of the board

		# Places the board onto the display at the very base coordinates (top left corner)
		self.ttt.blit(self.board, (0, 0))
		pygame.display.flip()  # Updates the entire display

	class Draw:

		class Board:

			def initialise_board(self):
				"""Job: Initialise the board and return the board as a variable."""

				# Setup background surface
				background = pygame.Surface(self.ttt.get_size())

				# Creates a surface object with the window size
				background = background.convert()  # Converts toe background to pixel format
				background.fill(WHITE)  # Converts the backgorund to a WHITE color (I think)

				# Draw Grid Lines

				# Vertical lines
				pygame.draw.line(background, (BLACK), (100, 0), (100, 300), 2)
				pygame.draw.line(background, (BLACK), (200, 0), (200, 300), 2)

				# horizontal lines...
				pygame.draw.line(background, (BLACK), (0, 100), (300, 100), 2)
				pygame.draw.line(background, (BLACK), (0, 200), (300, 200), 2)

				# Note about lines: Draws the lines with the Surface, Color, Start pos, End pos, and width

				return background  # returns the fully initialised background

		class Status:

			def draw_status(self):
				"""Job: Shows status at the bottom of the board (i.e player turn, num of moves, etc)
						In this case, board is the initialised game board where the status will be drawn onto."""

				message = self.game.game_message()
				# Setup (render) the message
				font = pygame.font.Font(None, 24)
				# Creates a default pygame font with the size of the font in pixels
				text = font.render(message, True, (BLACK))
				# Creates a new surface with the specified message on it.
				# It doesn't allow you to add to an existing surface, so we'll have to blit this surface onto our one.
				# After that, we set antialiasing to true. It then sets the color of the text to BLACK.

				# Send the finished status onto the board
				self.board.fill(WHITE, (0, 300, 300, 25))
				self.board.blit(text, (10, 300))
				# Pastes the status onto the board at the coordinates 10, 300

		class Symbols:

			def display_winning(self):
				win_state, value = self.game.game_won() # Gets the win state and value (i.e which row/column/diagonal)
				if win_state == "row":
					row = value
					pygame.draw.line(self.board, (RED), (0, (row + 1) * 100 - 50), (300, (row + 1) * 100 - 50), LINETHICKNESS)

				elif win_state == "column":
					col = value
					pygame.draw.line(self.board, (RED), ((col + 1) * 100 - 50, 0), ((col + 1) * 100 - 50, 300), LINETHICKNESS)

				elif win_state == "diag1":
					pygame.draw.line(self.board, (RED), (50, 50), (250, 250), LINETHICKNESS)

				elif win_state == "diag2":
					pygame.draw.line(self.board, (RED), (250, 50), (50, 250), LINETHICKNESS)

			def draw_move(self, board_row, board_col):
				"""Job: Draw either an X or an O (Symbol) on the board in a specific boardRow and boardCol
						Board is the game board surface we are drawing on. boardRow and boardCol are the row and column in which
						we will draw the symbol in. Symbol is either an X or an O, based on who's turn it is.
						Note: Lists are 0 based in terms of index. This means that if you call for the 0th item (i.e list[0]), you will
						get the first, as the index "starts" from 0."""

				Symbol = self.game.player_turn

				# Finds the center of the box we will draw in
				centerX = ((board_col) * CELL_DIMENSIONS) + (CELL_DIMENSIONS // 2)
				centerY = ((board_row) * CELL_DIMENSIONS) + (CELL_DIMENSIONS // 2)

				# Draws the appropriate symbol
				if Symbol == "O":  # If the Symbol is O, draw a circle in the specified square
					pygame.draw.circle(self.board, (BLACK), (centerX, centerY), 33, 2)
				elif Symbol == "X":
					# If the Symbol is X, draw two lines (i.e an X) in the specified square
					pygame.draw.line(self.board, (BLACK), (centerX - 22, centerY - 22), (centerX + 22, centerY + 22), 2)
					pygame.draw.line(self.board, (BLACK), (centerX + 22, centerY - 22), (centerX - 22, centerY + 22), 2)

				# Mark the square as occupied
				self.game.grid[board_row][board_col] = Symbol

if __name__ == "__main__":
	App()