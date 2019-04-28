import pygame
import sys
from viewmvc import View
from modelmvc import Model

class Controller:
    """Responsible for controlling everything behind the scenes and interpreting user input"""

    def __init__(self):
        """Not completely sure what should be here for now, but I'll keep this here anyway."""

        self.Game = Model()
        self.Graphics = View()
        self.play_game()
    def clicked_board(self):
        """Name isn't the best, I know. Finds the position of the mouse click and runs board_position.
        This allows it to find the exact cell. It then checks to see if that space is occupied. If not,
        it runs draw_move to draw a symbol there."""

        mouseX, mouseY = pygame.mouse.get_pos()  # Makes mouseX and mouseY equal to the coordinates of the mouse
        row, col = self.Game.find_cell(mouseX, mouseY) # board_position returns which row and column the user clicked in

        if self.Game.cell_occupied(col, row): # Checks to see if the space is full
            return # If it is, do nothing.
        else: # If it is
            self.Graphics.draw_move(self.Game.status, row, col, self.Game.CELL_DIMENSIONS) # Draw the Symbol onto the board
            self.Game.update_grid(row, col)
            self.Game.toggle_turn()

    def play_game(self):
        """Another brilliant name. This is the main game loop, where everything else is called."""
        while True:
            # Check to end the game
            if (self.Game.status == "X_Win") or (self.Game.status == "O_Win") or (self.Game.status == "Tie"):
                break

            self.check_for_event() # Checks to see if the window X button was pressed or if the user clicked
            self.Game.change_status() # Updates the status
            self.Game.choose_message()
            self.Graphics.draw_winning_line(self.Game.win_location) # Draws the winning line (if needed)
            self.Graphics.draw_status(self.Game.game_message) # Redraw the status with the new message
            self.Graphics.update_board() # Redraws the board

    def check_for_event(self):
        """Checks for events like QUIT and MOUSEBUTTONDOWN"""
        for event in pygame.event.get(): # Finds events that are currently queued up
            if event.type == pygame.QUIT:  # If the window close button is pressed
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: # If the mouse is clicked
                self.clicked_board() # Run clicked_board()


controller = Controller()
controller.play_game()