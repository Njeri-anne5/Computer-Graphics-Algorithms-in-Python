# This algorithm is used for scan converting a line. It was developed by Bresenham.
# It is an efficient method because it involves only integer addition, subtractions,
# and multiplication operations. These operations can be performed very rapidly so
# lines can be generated quickly.

# Learn about it here : https://www.javatpoint.com/computer-graphics-bresenhams-line-algorithm

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
twoDy = 2 * dy
twoDyDx = 2 * (dy - dx)
p = twoDy - dx

if x1 > x2:
	x = x2
	y = y2
	xend = x1
else:
	x = x1
	y = y1
	xend = x2

pixelArray = []
pixelArray.append((x,y))

while x < xend:
	x += 1

	if p < 0:
		p += twoDy
	else:
		y += 1
		p += twoDyDx
	pixelArray.append((x,y))

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