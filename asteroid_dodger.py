# My first non-terminal app
# On the internet they mostly use Tkinter for this type of apps. Let's see
from tkinter import *
from time import *
# Don't ask me why
from random import seed
# I get this one
from random import random

import math as m

SPEED  = 10
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
        everyOneIsDead = False
        while not(everyOneIsDead):
            self._canvas.update()
            self._canvas.delete(ALL)
            self._canvas.create_rectangle(0,0,WWIDTH, WHEIGHT, fill="#272727")
        
            for player in self._players:
                player.collisionCheck(self._asteroids)
                if not(player._isAlive):
                    everyOneIsDead = True
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

            self._canvas.create_text(WWIDTH/2, 150, text=str(self._players[0]._score), fill="#000", font=("sans-serif", 51))
            self._canvas.create_text(WWIDTH/2, 150, text=str(self._players[0]._score), fill="#fff", font=("sans-serif", 50))

            sleep(1/FRAMERATE)

            self._framecount += 1
        else:
            self._canvas.update()
            self._canvas.delete(ALL)
            self._canvas.create_rectangle(0,0,WWIDTH, WHEIGHT, fill="#272727")

            self._canvas.create_text(WWIDTH/2,WHEIGHT/2-200,fill="#fff", text="You died at score of", font=("sans-serif", 30))
            self._canvas.create_text(WWIDTH/2,WHEIGHT/2-100,fill="#fff", text=str(self._players[0]._score), font=("sans-serif", 50))
            self._canvas.create_text(WWIDTH/2,WHEIGHT/2,fill="#fff", text="Restart by pressing [space]", font=("sans-serif", 25))

            root.bind("<Key>", lambda a : self.reset(a))

    def reset(self, key):
        if key.keycode == 65:
             self.__init__(self._canvas, 1)

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
        self._isAlive = True
        self._score = 0

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

    def die(self):
        self._isAlive = False

    def collisionCheck(self, listOfAsteroids):
        hit = False
        for steroid in listOfAsteroids:
            if (steroid._posY+steroid._size/2 >= WHEIGHT-150) and (steroid._posY-steroid._size/2 <= WHEIGHT-50):
                if (steroid._posX-steroid._size/2 <= self._posX+25) and (steroid._posX+steroid._size/2 >= self._posX-25):
                    hit = True
                    break
                if (steroid._posX-steroid._size/2 >= self._posX+25) and (steroid._posX+steroid._size/2 <= self._posX-25):
                    hit = True
                    break
        
        if hit:
            self._color = "#f00"
            self.die()

        else:
            self._score += 1

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