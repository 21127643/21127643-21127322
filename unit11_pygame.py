import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Test unit11 part 1')
running = True
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
clock = pygame.time.Clock()

font = pygame.font.SysFont('sans', 30)
text = font.render("Random", True, BLACK)
text_box = text.get_rect()
circle_color = RED


while running == True:
	clock.tick(60)
	screen.fill(WHITE)

	mouse_x, mouse_y = pygame.mouse.get_pos()


	pygame.draw.rect(screen, WHITE, (50, 50, text_box[2], text_box[3]))

	screen.blit(text, (50, 50))

	pygame.draw.circle(screen, circle_color, (200, 300), 50)

	if 50 <= mouse_x <= 50 + (text_box[2]) and 50 <= mouse_y <= 50 + (text_box[3]):
		text = font.render("Random", True, BLUE)
		pygame.draw.line(screen, BLUE, (50, 50 + text_box[3]), (50 + text_box[2], 50 + text_box[3]))
	else:
		text = font.render("Random", True, BLACK)

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				if 50 <= mouse_x <= 50 + (text_box[2]) and 50 <= mouse_y <= 50 + (text_box[3]):
					circle_color = (randint(0, 255), randint(0, 255), randint(0, 255))
					print ("Click on red rect")


		if event.type == pygame.QUIT:
			running = False

	pygame.display.flip()

pygame.quit()