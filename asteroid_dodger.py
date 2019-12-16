# My first non-terminal app
# On the internet they mostly use Tkinter for this type of apps. Let's see
from tkinter import *
from time import *
# Don't ask me why
from random import seed
# I get this one
from random import random

import math as m

SPEED  = 5
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
        self._asteroids = []
        self._canvas = canvas
        self._framecount = 0

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
            self._canvas.delete(ALL)
            self._canvas.create_rectangle(0,0,WWIDTH, WHEIGHT, fill="#272727")
        
            for player in self._players:
                player.draw()


            if self._framecount % (2*FRAMERATE/3) == 0:
                newPosX = m.floor(random()*(WWIDTH-50)+25)
                #print(len(self._asteroids))

                if len(self._asteroids) >= 15:
                    del self._asteroids[:7]

                self._asteroids.append(Asteroid(newPosX, self._canvas))

                

            for steroid in self._asteroids:
                steroid.move()
                steroid.draw()

            sleep(1/FRAMERATE)

            self._framecount = self._framecount+1
            

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
        #print(side)
        if side.keysym == 'd':
            self.handleLeftMove()
        if side.keysym == 'a':
            self.handleRightMove()

    def handleLeftMove(self):
        if self._posX + 25 <= WWIDTH:
            #print(self._posX + 25)
            self._posX += SPEED
        #print("left")

    def handleRightMove(self):
        if self._posX - 25 >= 0:
            #print(self._posX - 25)
            self._posX -= SPEED
        #print("right")

    def draw(self):
        can = self._canvas
        can.create_rectangle(self._posX-25, WHEIGHT-150, self._posX+25, WHEIGHT-50, fill=self._color)


class Asteroid:
    def __init__(self, posX, canvas):
        self._posX = posX
        self._size = m.floor(random()*75)+25
        self._posY = -self._size/2
        self._canvas = canvas
    def draw(self):
        self._canvas.create_rectangle(
            self._posX - (self._size/2),  
            self._posY - (self._size/2), 
            self._posX + (self._size/2),
            self._posY + (self._size/2), 
            fill="#fff")
    def move(self):
        #print(self._posY)
        self._posY += 5


def __main__():
    runGame()

__main__()