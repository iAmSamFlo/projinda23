import time
from tetris import Figure
import random
import pygame

#This is where the mainGame loop and graphics are handled for tetris
pygame.init()

#Set up the screen
WIN_WIDTH = 800
WIN_HEIGHT = 600
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Tetris")

#Colors
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BlACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Main:
    level = 2 
    score = 0
    state = "start"
    field = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figure = None

    #Initialize the field
    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    def new_figure(self): #Create a new figure using the `__init__` function from `Figure
        self.figure = Figure(3, 0)

    def intersects(self): #Check if the figure intersects with the bottom or other blocks
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or \
                            j + self.figure.x > self.width - 1 or \
                            j + self.figure.x < 0 or \
                            self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersection = True
        return intersection

    def freeze(self): #Freeze the figure in place when it reaches the bottom using the `lock` function from `Figure`
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.break_lines()
        self.new_figure()
        if self.intersects():
            self.state = "gameover"

    def break_lines(self): #Break lines when they are full, this is where the score is calculated and the figures above move down one row
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i2 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i2][j] = self.field[i2 - 1][j]
        self.score += lines ** 2
    
    def go_space(self): #Move the figure all the way down when spacebar is pressed using the `move_down` function from `Figure`
        while not self.intersects():
            self.figure.y += 1
        self.figure.y -= 1
        self.freeze()

    def go_down(self): #Move the figure one block down using the `move_down` function from `Figure`
        self.figure.y += 1
        if self.intersects():
            self.figure.y -= 1
            self.freeze()
    
    def go_side(self, dx): #Move the figure one block to the side using the `move_left` and `move_right` functions from `Figure`
        old_x = self.figure.x
        self.figure.x += dx
        if self.intersects():
            self.figure.x = old_x

    def rotate(self): #Rotate the figure using the `rotate` function from `Figure`
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

        

#Frames per second
fps = 30

clock = pygame.time.Clock()

#Check if the game has started
started = False

run = True

game = Main(20, 10)
counter = 0

pressing_down = False

font = pygame.font.SysFont('comicsans', 25, True, False)
font2 = pygame.font.SysFont('comicsans', 50, True, False)
 #Main game loop
while run:
    clock.tick(fps) 

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                started = True
            elif event.key == pygame.K_ESCAPE:
                run = False

    # Draw the start window
    if not started and game.state == "start":
        WIN.fill(WHITE)
        start_text = font.render("Press ENTER to start", 1, RED)
        tetris = font2.render("Tetris", 1, BLUE)
        start_image = pygame.image.load('start_pic.png')
        WIN.blit(start_image, (166, 50))
        WIN.blit(tetris, (320, -10))
        WIN.blit(start_text, (265, 515))
        pygame.display.update()
        continue

    #Check if the game has started
    if started:
        if game.figure is None:
                game.new_figure()
            
        counter += 1 

        if counter > 100000:
            counter = 0

        if counter % (fps // game.level // 2) == 0 or pressing_down: #Increase the speed of the game
            if game.state == "start":
                game.go_down()

        #Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
                time.sleep(0.1)
            if event.key == pygame.K_DOWN:
                game.go_down()
            if event.key == pygame.K_LEFT:
                game.go_side(-1)
                time.sleep(0.1)
            if event.key == pygame.K_RIGHT:
                game.go_side(1)
                time.sleep(0.1)

            #Min space bar funkar inte för mig /Samflo
            if event.key == pygame.K_LSHIFT  or event.key == pygame.K_RSHIFT:
                print("space check")
                game.go_space()
                time.sleep(0.2)

            if event.key == pygame.K_ESCAPE:
                run = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                pressing_down = False

        #Draw the background
        WIN.fill(BlACK)

        #Draw the grid and the field
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(WIN, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(WIN, Figure.colors[game.field[i][j]],
                                    [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])

        #Draw the current figure using the `image` function from `Figure`
        if game.figure is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.figure.image():
                        pygame.draw.rect(WIN, Figure.colors[game.figure.color],
                                        [game.x + game.zoom * (j + game.figure.x) + 1,
                                        game.y + game.zoom * (i + game.figure.y) + 1,
                                        game.zoom - 2, game.zoom - 2])

        #Draw the score, level and game over text
        text = font.render("Score: " + str(game.score), True, RED)
        text_over = font2.render("Game Over", True, RED)
        text2_over = font2.render("Press ESC to quit", True, RED)

        #Draw the text on the screen
        WIN.blit(text, [0, 0])
        
        if game.state == "gameover": #Draw the game over text
            WIN.blit(text_over, [20, 200])
            WIN.blit(text2_over, [20, 300])
            started = False
            game = Main(20, 10)
            counter = 0
            pressing_down = False
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
