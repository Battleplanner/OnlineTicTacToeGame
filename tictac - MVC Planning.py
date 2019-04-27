"""The goal of this is to use MVC (Mode, View, Contoller) as a way of designing the project.
My first goal should ideally be how I should organise things (i.e which functions go where, and do what)

"""

# View = Responsible for graphics
# Model (i.e Game) = Responsible for game logic and rules
# Controller = Responsible for user input and giving commands to Model and View

# Other notes: After controller calls for View to draw the move, it needs to change grid to accept that move


class View:
    """Is responsible for dealing with everything the user sees (i.e GUI)"""

    def create_board(self): # Could be replaced to be __init__ instead if thats better...
        """Creates the board surface"""
        pass

    def initialise_window(self): # Could be merged with create_board to make __init___...
        """Initialises/creates the window"""

    def update_board(self):
        """You guessed it! Updates the surface by redrawing the board onto it. Gets board from Model."""
        pass

    def draw_status(self):
        """Updates the status with info on who's turn it is and who's won. Will recieve the message from Model"""
        pass

    def draw_winning_line(self):
        """Draws the line that represents a win. Receives info about who won (and where) from Model"""
        pass

    def draw_move(self):
        """Draws either an X or an O on a specific row and column on the board. Recieves who and where from Controller"""
        pass
class Game:
    """This is the Model. Here, all the game data and logic is held"""

    def __init__(self):
        """Initialises game variables, such as the grid, player turn, etc"""
        pass

    def board_full(self): # Note. This may belong under control...
        """Checks to see if the board is full, and returns True or False. """
        pass

    def game_message(self):
        """Determines what the game message is, based on whether someone's won, who's turn it is, or if it's a tie."""
        pass

    def game_over(self):
        """Checks to see if the game is over, whether that was by a tie or a player win."""
        pass

    def cell_empty(self):
        """Checks to see if a cell is empty (Necessary in order to only draw if the space is not occupied"""
        pass

    def toggle_turn(self):
        """Toggles the turn. Not much to it really."""

    @staticmethod
    def board_position(mouseX, mouseY):
        """Responsible for finding out which board space (i.e row, column) the user clicked in based on
        their mouse coordinates. Doesn't require self, as long as Controller gives it mouseX and mouseY."""
        pass


class Controller:
    """Responsible for controlling everything behind the scenes and interpreting user input"""

    def __init__(self):
        """Not completely sure what should be here for now, but I'll keep this here anyway."""
        pass

    def clicked_board(self):
        """Name isn't the best, I know. Finds the position of the mouse click and runs board_position.
        This allows it to find the exact cell. It then checks to see if that space is occupied. If not,
        it runs draw_move to draw a symbol there."""
        pass

    def play_game(self):
        """Another brilliant name. This is the main game loop, where everything else is called."""
        pass

    def check_for_event(self):
        """Checks for events like QUIT and MOUSEBUTTONDOWN"""
        pass