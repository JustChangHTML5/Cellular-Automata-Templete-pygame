import pygame, GameMatrix

pygame.init()

width = 105
height = 60
gridSize = 13
size = (width * gridSize, height * gridSize)
screen = pygame.display.set_mode(size)
isRunning = False
framebyframe = False
showGrid = True
#display setting, change them if you want!
cellColors = ((230, 230, 230))
#add any other colors inside the tuple!
Game = GameMatrix.Matrix()
GameFlip = GameMatrix.Matrix()
Game.build(width, height)
GameFlip.build(width, height)
pygame.display.set_caption("Cellular Automata", "CA")
icon = pygame.image.load("TheCircuitToy.jpg")
pygame.display.set_icon(icon)