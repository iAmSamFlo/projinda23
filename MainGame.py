import sys
import pygame
import cv2

#I terminalen: pip install opencv-python

#This is where the mainGame loop and graphics are handled for tetris

pygame.init()

#Set up the screen
WIN_WIDTH = 640
WIN_HEIGHT = 480
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tetris")


#Set up background video
cap = cv2.VideoCapture('Background.mp4')
success, img = cap.read()
shape = img.shape[1::-1]
wn = pygame.display.set_mode(shape)


clock = pygame.time.Clock()


WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BlACK = (0, 0, 0)
RED = (255, 0, 0)

def drawWindow(img):
    WIN.fill(BlACK)
    
    wn.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
    WIN.blit(pygame.font.SysFont('comicsans', 60).render('TETRIS', 1, RED), (200, 200))
    pygame.display.update()

fps = 30

#game loop
def main():
    
    run = True
    
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

        # Draw window
        drawWindow(img)

#Om jag förstår rätt så är det här en restraint så att man inte kan köra programmet utanför main funktionen eller MainGame.py filen
if __name__ == "__main__":
    main()
    
pygame.quit()
sys.exit()
    
