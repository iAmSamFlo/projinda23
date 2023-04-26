import sys
import pygame

#This is where the mainGame loop and graphics are handled for tetris

pygame.init()

#Set up the screen
WIN = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tetris")


clock = pygame.time.Clock()
fps = 60

#game loop
def main():

    run = True
    while run:
    #want to handle what happens
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
                

        WIN.fill((0,0,0))

        pygame.display.flip()

        clock.tick(fps)

    
#Om jag förstår rätt så är det här en restraint så att man inte kan köra programmet utanför main funktionen eller MainGame.py filen
if __name__ == "__main__":
    main()