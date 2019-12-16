# My first non-terminal app
# On the internet they mostly use Tkinter for this type of apps. Let's see
from tkinter import *
from time import *

SPEED  = 3.14
WWIDTH = 500
WHEIGHT = 1000
FRAMERATE = 60

root =  Tk()


# Goal of the game is to press A or D and dodge asteroids for as long as possible.
# I will attempt to apply my experience with JS canvas and JS apps in general
def runGame(): 
    # this is how they call main window on the internet. I guess it's right
    global root
    # if I understand it correctly AxB defines A width and B height of the window
    root.geometry(str(WWIDTH)+"x"+str(WHEIGHT))

    # this should disable resizability (I hope) on both axis' right?
    root.resizable(False, False)

    # Renaming the window
    root.title("Asteroid dodger")

    c = Canvas(root, width=WWIDTH, height=WHEIGHT, bd=0, highlightthickness=0)
    c.pack()

    # Calling game to start
    currentGame = Game(c, 1)


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
    def __init__(self, canvas, amount_of_players):
        # So I read on the internet that it is "self" and not "this" and also you are supposed to call attributes with an underscore. IDK why
        self._time = 0;
        self._amount_of_players = amount_of_players
        self._players = []
        self._canvas = canvas

        # let's make it black as in space would be
        canvas.create_rectangle(0,0,WWIDTH, WHEIGHT, fill="#272727")

        # creating players
        for p in range(amount_of_players):
            self._players.append(Player("John Snow", "#fff", canvas))
        
        for player in self._players:
            player.draw()

        self.refresh()

    def refresh(self):
        while True:
            self._canvas.update()
            self._canvas.create_rectangle(0,0,WWIDTH, WHEIGHT, fill="#272727")
        
            for player in self._players:
                #player.moveLeft(1)
                player.draw()
            sleep(1/FRAMERATE)
            

    def movePlayersLeft(self):
        for player in self._players:
            player.move('left')
        
    def movePlayersRight(self):
        for player in self._players:
            player.move('right')


class Player:
    def __init__(self, name, color, canvas):
        global root
        self._name = name
        self._color = color
        self._posX = WWIDTH/2
        self._canvas = canvas

        #<Key> gives me: <KeyPress event state=Mod2 keysym=value keycode=generalKeyCode char='value' x=mousePosX y=mousePosY> when used in lambda
        root.bind('<Key>', lambda a : self.move(a))
        #root.bind('d', self.moveRight)

    # Why do ALL the methods need self as the first argument
    def move(self, side):
        print(side)
        if side.keysym == 'd':
            self.handleLeftMove()
        if side.keysym == 'a':
            self.handleRightMove()

    def moveLeft(self):
        print("Left")
        self._posX -= 3
        #root.bind('a', self.moveLeft)

    def moveRight(self):
        print("Right")
        self._posX += 3
        #root.canvas.bind('d', self.moveRight)

    def handleLeftMove(self):
        self._posX += SPEED
        #print("left")

    def handleRightMove(self):
        self._posX -= SPEED
        #print("right")

    def draw(self):
        can = self._canvas
        can.create_rectangle(self._posX-25, WHEIGHT-150, self._posX+25, WHEIGHT-50, fill=self._color)


def __main__():
    runGame()

__main__()