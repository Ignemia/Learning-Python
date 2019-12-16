from tkinter import *
from time import *
from random import seed
from random import random
import math as m

SPEED  = 10
WWIDTH = 500
WHEIGHT = 1000
FRAMERATE = 60

root =  Tk()

def runGame(): 
    global root
    root.geometry(str(WWIDTH)+"x"+str(WHEIGHT))
    root.resizable(False, False)
    root.title("Asteroid dodger")
    c = Canvas(root, width=WWIDTH, height=WHEIGHT, bd=0, highlightthickness=0)
    c.pack()
    currentGame = Game(c, 1)
    root.mainloop()
class Game:
    def __init__(self, canvas, amount_of_players):
        self._time = 0;
        self._amount_of_players = amount_of_players
        self._players = []
        self._asteroids = []
        self._canvas = canvas
        self._framecount = 0

        canvas.create_rectangle(0,0,WWIDTH, WHEIGHT, fill="#272727")
        
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

        root.bind('<Key>', lambda a : self.move(a))

    def move(self, side):
        if side.keysym == 'd':
            self.handleLeftMove()
        if side.keysym == 'a':
            self.handleRightMove()

    def handleLeftMove(self):
        if self._posX + 25 <= WWIDTH:
            self._posX += SPEED

    def handleRightMove(self):
        if self._posX - 25 >= 0:
            self._posX -= SPEED

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
        self._posY += 5


def __main__():
    runGame()

__main__()