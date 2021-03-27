# A program to set pixel value of selected point on the screen

import pygame

pygame.init()
SIZE = WIDTH, HEIGHT = (500, 500)
win = pygame.display.set_mode(SIZE)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

running = True
pixelArray = []
while running:
	win.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pos = pygame.mouse.get_pos()
				pixelArray.append(pos)

	for pixel in pixelArray:
		win.set_at(pixel, WHITE)

	pygame.display.update()

pygame.quit()