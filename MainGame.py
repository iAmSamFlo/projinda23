import pygame

#This is where the mainGame loop and graphics are handled for tetris

pygame.init()

#Set up the screen
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tetris")


clock = pygame.time.Clock()
fps = 60

#game loop
while True:
    #want to handle what happens
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    pygame.display.flip()

    clock.tick(fps)

