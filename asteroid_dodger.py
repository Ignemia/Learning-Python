# My first non-terminal app
# On the internet they mostly use Tkinter for this type of apps. Let's see
from tkinter import *

SPEED  = 1
WWIDTH = 500
WHEIGHT = 1000

# Goal of the game is to press A or D and dodge asteroids for as long as possible.
# I will attempt to apply my experience with JS canvas and JS apps in general
def runGame(): 
    # this is how they call main window on the internet. I guess it's right
    root =  Tk()

    # if I understand it correctly AxB defines A width and B height of the window
    root.geometry(str(WWIDTH)+"x"+str(WHEIGHT))

    # this should disable resizability (I hope) on both axis' right?
    root.resizable(False, False)

    # Renaming the window
    root.title("Asteroid dodger")

    # Calling game to start
    currentGame = Game(1)

    #This makes the window not disappear immediatelly
    root.mainloop()
    """
    So this is how you make multiline comments huh
    """

# I'm scared that it is going to be difficult to work with classes in Python
class Game:
    """
        First thing I did was that I forgot to use "def" keyword when defining constructor
        Second thing I did was that I forgot that it is called "__init__" and not constructor
        Third thing I don't even know because it waqs so dumb that I forgot it.
        I need more practice
        Can anyone explain to me why is there "self" as first argument?
    """
    def __init__(self, amount_of_players):
        # So I read on the internet that it is "self" and not "this" and also you are supposed to call attributes with an underscore. IDK why
        self._time = 0;
        self._amount_of_players = amount_of_players



class Player:
    def __init__(self, name, color):
        self._name = name
        self._color = color
        self._posX = WWIDTH/2

    # Why do ALL the methods need self as the first argument
    def move(self, side):
        if side == 'left':
            self.handleLeftMove()
        if side == 'right':
            self.handleRightMove()

    def handleLeftMove(self):
        self._posX += SPEED
    def handleRightMove(self):
        self._posX -= SPEED


def __main__():
    runGame()

__main__()