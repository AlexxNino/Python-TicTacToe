import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))

background = pygame.image.load('Background.png')

pygame.display.set_caption("Tic-Tac-Toe")

stuff =['','','','','','','','','','']


def mouse_event(turn):
	x,y = pygame.mouse.get_pos()
	
	#print(x,y)

	#Top Row
	if x < 200 and y < 200:
		x = 0
		y = 0
		if stuff[0] != 1 or stuff[0] != 0:
			print(turn)
			if turn == 1:
				stuff[0]=1
			if turn == 0:
				stuff[0]=0
	if x > 200 and x < 400 and y < 200:
		x = 200
		y = 0
		if stuff[1] != 1 or stuff[1] != 0:
			if turn == 1:
				stuff[1]=1
			if turn == 0:
				stuff[1]=0
	if x > 400 and y < 200:
		x = 400
		y = 0
		if stuff[2] != 1 or stuff[2] != 0:
			if turn == 1:
				stuff[2]=1
			if turn == 0:
				stuff[2]=0
	

	#Middle Row
	if x < 200 and y < 400 and y > 200:
		x = 0
		y = 200
		if stuff[3] != 1 or stuff[3] != 0:
			if turn == 1:
				stuff[3]=1
			if turn == 0:
				stuff[3]=0
	if x < 400 and x > 200 and y < 400 and y > 200:
		x = 200
		y = 200
		if stuff[4] != 1 or stuff[4] != 0:
			if turn == 1:
				stuff[4]=1
			if turn == 0:
				stuff[4]=0	
	if x < 600 and y < 400 and y > 200:
		x = 400
		y = 200
		if stuff[5] != 1 or stuff[5] != 0:
			if turn == 1:
				stuff[5]=1
			if turn == 0:
				stuff[5]=0
	

	#Bottom Row
	if x < 200 and y > 400:
		x = 0
		y = 400	
		if stuff[6] != 1 or stuff[6] != 0:
			if turn == 1:
				stuff[6]=1
			if turn == 0:
				stuff[6]=0
	if x > 200 and x < 400 and y > 400:
		x = 200
		y = 400
		if stuff[7] != 1 or stuff[7] != 0:
			if turn == 1:
				stuff[7]=1
			if turn == 0:
				stuff[7]=0
	if x > 400 and y > 400:
		x = 400
		y = 400
		if stuff[8] != 1 or stuff[8] != 0:
			if turn == 1:
				stuff[8]=1
			if turn == 0:
				stuff[8]=0
	
	print(stuff)

	if turn == 0:
		load_x(x,y)
	if turn == 1:
		load_o(x,y)
	turn+=1
	


def load_x(x,y):
	ximg = pygame.image.load('x.png')
	screen.blit(ximg,(x,y))
	pygame.display.update()

def load_o(x,y):
	oimg = pygame.image.load('o.png')
	screen.blit(oimg,(x,y))
	pygame.display.update()

def main():
	running = True
	turn = 0
	lastx = 0
	lasty = 0
	winner = False
	screen.blit(background,(0,0))
	pygame.display.update()
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		if event.type == pygame.MOUSEBUTTONUP:
			x,y = pygame.mouse.get_pos()
			if x == lastx and y == lasty:
				None
			else:
				mouse_event(turn%2)
				turn+=1
				lastx = x
				lasty = y


main()