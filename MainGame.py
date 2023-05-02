import random
import sys
import pygame
import cv2

from tetris import Figure

#I terminalen: pip install opencv-python

#This is where the mainGame loop and graphics are handled for tetris

pygame.init()

#Set up the screen
WIN_WIDTH = 1280
WIN_HEIGHT = 720
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tetris")

#Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BlACK = (0, 0, 0)
RED = (255, 0, 0)

#To be changed
delay = 1000

#Draws the window
def drawWindow(started):
    WIN.fill(BlACK)
    
    

    if not started:
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (100, 100))
        WIN.blit(pygame.font.SysFont('comicsans', 40).render('Press SPACE to start playing', 1, RED), (400, 600))
    else:
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (100, 100))
        Figure.blocks(delay)
    
    pygame.draw.rect(WIN, RED, (515, -1, 250, 501), 1) #640 e mitten av skärmen. 
    #Fabian säger att en cell är 25, vilket då menar att bredden blir 250 och höjd blir 500.

    pygame.display.update()

#Tick rate
fps = 30

figure = Figure(100, 0)

#game loop
def main():
    clock = pygame.time.Clock()
    run = True

    #Check if the game has started
    started = False
    
    while run:
        clock.tick(fps)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()

        if not started:
            if keys_pressed[pygame.K_SPACE]:
                started = True
                print("Game started")
        

        if keys_pressed[pygame.K_LEFT]:
            print("Left arrow pressed")
        if keys_pressed[pygame.K_RIGHT]:
            print("Right arrow pressed")
        if keys_pressed[pygame.K_UP]:
            print("Up arrow pressed")
        if keys_pressed[pygame.K_DOWN]:
            print("Down arrow pressed")

        # Draw window
        drawWindow(started)

#Om jag förstår rätt så är det här en restraint så att man inte kan köra programmet utanför main funktionen eller MainGame.py filen
if __name__ == "__main__":
    main()
    
pygame.quit()
sys.exit()