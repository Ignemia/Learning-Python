# My first non-terminal app
# On the internet they mostly use Tkinter for this type of apps. Let's see
from tkinter import *

# Goal of the game is to press A or D and dodge asteroids for as long as possible.
# I will attempt to apply my experience with JS canvas and JS apps in general
def runGame(): 
    # this is how they call main window on the internet. I guess it's right
    root =  Tk()

    # if I understand it correctly AxB defines A width and B height of the window
    root.geometry("500x1000")

    # this should disable resizability (I hope)
    root.resizable = False

    #This makes the window not disappear immediatelly
    root.mainloop()
    

def __main__():
    runGame()