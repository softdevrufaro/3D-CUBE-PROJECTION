import pygame as pg  
from cube import cube
from pygame.time import Clock
# Initializing pygame 
pg.init()
# Initializing the screen
screen = pg.display.set_mode((800 , 600))
# Creating the flag to control the game running 
running = True 
# creating a cube instance 
cube_1 = cube([ 150 , 300 , 200] , 100)
cube_1.rotation = [0 , 0 , 0]
# Game clock
clock = Clock()
# Making the main loop 
while running: 
	screen.fill((0 , 0 , 0))
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			running = False
	cube_1.display(screen)
	cube_1.rotation[0] += 0.01 # rotation along the x-axis
	cube_1.rotation[1] += 0.01 # rotation along the y-axis
	cube_1.rotation[2] += 0.01 # rotation along the z-axis
	clock.tick(30)
	pg.display.update()

print("Goodbye")