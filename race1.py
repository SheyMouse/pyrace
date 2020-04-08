from random import randint
import pgzrun

WIDTH = 700 #Width of the game area
HEIGHT = 800 # Height of the game area
car = Actor("racecar") # Load in the actor image
car.pos = 250, 700 # set the car position
SPEED = 4
trackCount = 0
trackPosition = 250
trackWidth = 120
trackDirection = False
trackLeft = [] # list of track barriers left
trackRight = [] # list of track barriers right
gameStatus = 0