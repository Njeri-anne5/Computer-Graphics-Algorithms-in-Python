# The digital diffrential analyzer is a scan conversion line algorithm based on calculating ▲y or ▲x using the cartesian slope
# intercept equation.

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = (500, 500)
win = pygame.display.set_mode(SIZE)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Algorithm -------------------------------------------------------------------

x1, y1 = starting_pos = (100, 100)
x2, y2 = ending_pos = (250, 250)

dx = x2 - x1
dy = y2 - y1

if abs(dx) > abs(dy):
	steps = abs(dx)
else:
	steps = abs(dy)

x_increment = dx / steps
y_increment = dy / steps

pixelArray = []
x, y = x1, y1
pixelArray.append((x,y))

for k in range(steps):
	x += x_increment
	y += y_increment
	pixelArray.append((int(x),int(y)))

# Displaying result on screen -------------------------------------------------

running = True
while running:
	win.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for pixel in pixelArray:
		win.set_at(pixel, WHITE)

	pygame.display.update()

pygame.quit()