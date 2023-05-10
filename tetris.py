import random
import sys
import pygame

white = (255, 255, 255)
block_size = 25 

class Figure:
    x = 0 #Horizontal position of the block
    y = 0 #Vertical position of the block

    colors = [ #All possible colors of the tetrominos
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (178, 255, 102),  
    ]
    figures =[
        [[4, 5, 6, 7], [2, 6, 10, 14], [8, 9, 10, 11], [1, 5, 9, 13]], #I-block
        [[1, 4, 5, 6], [1, 5, 6, 9], [4, 5, 6, 9], [1, 4, 5, 9]], #T-block
        [[1, 2, 4, 5], [1, 5, 6, 10], [5, 6, 8, 9], [0, 4, 5, 9]], #S-block1
        [[0, 1, 5, 6], [2, 5, 6, 9], [4, 5, 9, 10], [1, 4, 5, 8]], #S-block2
        [[1, 2, 5, 6]], #O-block
        [[0, 4, 5, 6], [1, 2, 5, 9], [4, 5, 6, 10], [1, 5, 8, 9]], #L-block1
        [[2, 4, 5, 6], [1, 5, 9, 10], [4, 5, 6, 8], [0, 1, 5, 9]], #L-block2
 
    ] 
    
    #Type, color and rotation of block generated randomly at the start of the game
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(Figure.colors) - 1)
        self.rotation = 0

            
    def image(self): #returns the current state of the figure as an image on the board
        return self.figures[self.type][self.rotation]
      
    def rotate(self): #rotate the figure to the next rotation (clockwise)
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        
    def move_left(self): #move the figure one block to the left
        self.x -= block_size
    
    def move_right(self): #move the figure one block to the right
        self.x += block_size
        
    def lock(self): #locks the figure in place, when it reaches the bottom
        self.locked = True
    
    def move_down(self): #moves the figure one block down
        for i in range(len(self.y)):
            self.y[i] += self.dy
        
    def spawn(self): #spawns a new figure, when the current one reaches the bottom
        self.type = random.randint(0, len(self.figures) - 1)
        self.rotation = 0
        self.current_block = self.figures[self.type][self.rotation]
        self.x = 4
        self.y = [0] * 4
        self.color = random.randint(0, len(self.colors))
        self.locked = False
    
    def get_blocks(self): #draws the current state of the figure on the board, returns a list of x, y values and color
        blocks = []
        for i, block in enumerate(self.image):
            x = (block % 4) * block_size + self.x
            y = (block // 4) * block_size + self.y[i]
            blocks.append(((x, y), self.colors))
        return blocks        