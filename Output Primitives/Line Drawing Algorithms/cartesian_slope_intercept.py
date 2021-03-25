# A program to create a line segment between two points using the Cartesian Slope Intercept Equation.
# Cartesian Slope Intercept Equation : y = m*x + b
# m = y2 - y1 / x2 - x1
# b = y1 - m * x1

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = (500, 500)
win = pygame.display.set_mode(SIZE)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

x1, y1 = starting_pos = (100, 100)
x2, y2 = ending_pos = (250, 250)

m = (y2 - y1) / (x2 - x1)
b = y1 -  m * x1

pixelArray = []
for x in range(x1, x2 + 1):
	y = int(m * x)
	pixelArray.append((x,y))

running = True
while running:
	win.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	for pixel in pixelArray:
		win.fill(WHITE, (pixel, (1, 1)))
		# win.set_at(pixel, WHITE)

	pygame.display.update()

pygame.quit()