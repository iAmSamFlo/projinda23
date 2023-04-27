import sys
import pygame
import cv2

#I terminalen: pip install opencv-python

#This is where the mainGame loop and graphics are handled for tetris

pygame.init()

#Set up the screen
WIN_WIDTH = 600
WIN_HEIGHT = 480
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tetris")


#Set up background video
cap = cv2.VideoCapture('Background.mp4')
success, img = cap.read()
shape = img.shape[1::-1]

#Change the shape of the window to the video
wn = pygame.display.set_mode(shape)



#Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BlACK = (0, 0, 0)
RED = (255, 0, 0)

#Draws the window
def drawWindow(img, started):
    WIN.fill(BlACK)
    
    wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))

    if not started:
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (100, 100))
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('Press SPACE to start playing', 1, RED), (400, 600))
    else:
        WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (100, 100))
    
    pygame.draw.rect(WIN, WHITE, (515, -1, 250, 501), 1) #640 e mitten av skärmen. 
    #Fabian säger att en cell är 25, vilket då menar att bredden blir 250 och höjd blir 500.

    pygame.display.update()

#Tick rate
fps = 30



#game loop
def main():
    clock = pygame.time.Clock()
    run = True

    #Check if the game has started
    started = False
    
    while run:
        clock.tick(fps)

        # Read frame from video stream
        success, img = cap.read()

        # Check if end of video stream
        if not success:
            # Restart video stream from the beginning
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success, img = cap.read()

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
        drawWindow(img, started)

#Om jag förstår rätt så är det här en restraint så att man inte kan köra programmet utanför main funktionen eller MainGame.py filen
if __name__ == "__main__":
    main()
    
pygame.quit()
sys.exit()