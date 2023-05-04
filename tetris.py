import random
import sys
import pygame

white = (255, 255, 255)
block_size = 25

class Figure:
    x = 0
    y = 0

    colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (178, 255, 102),  
    ]
    figures =[
        [[4, 5, 6, 7], [1, 5, 9, 13]], #I-block
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], #T-block
        [[1, 2, 5, 4], [1, 5, 6, 10], [1, 2, 6, 7], [3, 6, 7, 10]], #S-block
        [[1, 2, 5, 6]], #O-block
        [[1, 5, 6, 7], [3, 5, 6, 7], [1, 2, 6, 10], [3, 2, 6, 10], [1, 5, 9, 8], [1, 5, 9, 10], [4, 5, 6, 10], [4, 5, 6, 8]], #L-block
 
    ] 
    
    #Type and color of block generated randomly
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(1, len(Figure.colors) - 1)
        self.rotation = 0

        '''
        self.color = (255, 255, 255)
        self.rotation = 0
        self.dy = block_size
        self.locked = False
        
        self.current_block = self.figures[self.type][self.rotation]'''
        
    """ 
    def blocks(delay):
        if not figure.locked:
            #Update each block of the figure and reset it at the top if it reaches the bottom
            for i, block in enumerate(figure.image()):
                x = (block % 4) * block_size + figure.x
                y = (block // 4) * block_size + figure.y[i]
                pygame.draw.rect(WIN, figure.color, (x, y, block_size, block_size))
                figure.y= [y + figure.dy for y in figure.y]
                
                if y >= screen_height - block_size:
                    figure.locked = True
                    break
            
            pygame.time.delay(delay)

            # if figure.y[i] >= 480:
            #     figure.y[i] = 0
            #     figure.type = random.randint(0, len(figure.figures) - 1)
            #     figure.color = (255, 255, 255) """
            
    def image(self):
        return self.figures[self.type][self.rotation]
      
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        #self.current_block = self.figures[self.type][self.rotation]
        
    def move_left(self):
        self.x -= block_size
    
    def move_right(self):
        self.x += block_size
        
    def lock(self):
        self.locked = True
    
    def move_down(self):
        for i in range(len(self.y)):
            self.y[i] += self.dy
        
    def spawn(self):
        self.type = random.randint(0, len(self.figures) - 1)
        self.rotation = 0
        self.current_block = self.figures[self.type][self.rotation]
        self.x = 4
        self.y = [0] * 4
        self.color = (255, 255, 255)
        self.locked = False
    
    def get_blocks(self):
        blocks = []
        for i, block in enumerate(self.image):
            x = (block % 4) * block_size + self.x
            y = (block // 4) * block_size + self.y[i]
            blocks.append(((x, y), self.colors))
        return blocks        