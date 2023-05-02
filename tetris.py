import random
import sys
import pygame
pygame.init()
screen_width = 600
screen_height = 480
white = (255, 255, 255)
screen = pygame.display.set_mode((screen_width, screen_height))
WIN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
fps = 1

class Figure:
    colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (178, 255, 102),  
    ]
    figures =[
        [[4, 5, 6, 7], [1, 5, 9, 13]], #I-block
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], #T-block
        [[1, 2, 5, 4], [1, 5, 6, 10], [1, 2, 6, 7], [3, 6, 7, 10]], #S-block
        [[1, 2, 5, 6]] #O-block     
    ] 
    
    #Type and color of block generated randomly
    def __init__(self, x, y):
        self.x = x
        self.y = [0] * 4
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = (255, 255, 255)
        self.rotation = 0
        self.dy = 25
    
    def image(self):
        return self.figures[self.type][self.rotation]  
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
    def blocks(delay):
            #Update each block of the figure and reset it at the top if it reaches the bottom
        for i, block in enumerate(figure.image()):
            x = (block % 4) * 25 + figure.x
            y = (block // 4) * 25 + figure.y[i]
            pygame.draw.rect(screen, figure.color, (x, y, 25, 25))
            figure.y[i] += figure.dy
        
        pygame.time.delay(delay)

        if figure.y[i] >= 480:
            figure.y[i] = 0
            figure.type = random.randint(0, len(figure.figures) - 1)
            figure.color = (255, 255, 255)


figure = Figure(100, 0)
    
 
        
    
            