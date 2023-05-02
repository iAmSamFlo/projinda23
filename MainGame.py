from tetris import Figure
import random
import sys
import pygame




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
delay = 500

block_size = 25

# List of locked figures
locked_figures = []
# List of locked blocks
locked_blocks = []

def add_to_board(figures_blocks, locked_blocks):
    for block in figures_blocks:
        locked_blocks.append(block)

#Draws the window
def drawWindow(started, locked_figures):
    WIN.fill(BlACK)
    
    

    if not started:
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (100, 100))
        WIN.blit(pygame.font.SysFont('comicsans', 40).render('Press SPACE to start playing', 1, RED), (400, 600))
    else:
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (100, 100))

        # Draw the locked figures / and land figures?
        for blocks in locked_figures:
            for x, y in blocks:
                pygame.draw.rect(WIN, RED, (x, y, block_size, block_size))
        add_to_board(figure.get_blocks(), locked_figures)
        
        if not figure.locked:
            for i, block in enumerate(figure.get_blocks()):
                x = (block % 4) * block_size + figure.x
                y = (block // 4) * block_size + figure.y[i]
                pygame.draw.rect(WIN, figure.color, (x, y, block_size, block_size))
            
            # Update the y coordinate of each block
            figure.y = [y + figure.dy for y in figure.y]
            for y in figure.y:
                if y >= WIN_HEIGHT - block_size:
                    figure.locked = True
                    break
                
        if figure.locked:
            # Lock the figure in place and spawn a new one
            Figure.get_blocks(figure) 
            figure.spawn()
            figure.locked = False
    
    pygame.draw.rect(WIN, RED, (515, -1, 250, 501), 1) #640 e mitten av skärmen. 
    #Fabian säger att en cell är 25, vilket då menar att bredden blir 250 och höjd blir 500.

    pygame.display.update()


    

#Frames per second
fps = 30

#figure = Figure(100, 0)

#game loop
def main():
    global figure
    
    clock = pygame.time.Clock()
    run = True

    #Check if the game has started
    started = False
    
    # Initialize the figure object
    figure = Figure(WIN_HEIGHT // 2)
   
    
    # List of locked figures
    locked_figures = [] 
    
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
                figure.move_left()
                print("Left arrow pressed")
            if keys_pressed[pygame.K_RIGHT]:
                figure.move_right()
                print("Right arrow pressed")
            if keys_pressed[pygame.K_UP]:
                figure.rotate()
                print("Up arrow pressed")
            if keys_pressed[pygame.K_DOWN]:
                figure.dy = 50
                print("Down arrow pressed")
                

        # Draw window
        drawWindow(started, locked_figures)
        
        if figure.locked:
            locked_figures.append(figure.get_blocks())
            figure = Figure(WIN_HEIGHT // 2, 0)
        if not run:
            break
    
#Om jag förstår rätt så är det här en restraint så att man inte kan köra programmet utanför main funktionen eller MainGame.py filen
if __name__ == "__main__":
    main()
    pygame.quit()
    sys.exit()   
