import random
import pygame
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (178, 255, 102),  
]
class Figure:
    figures =[
        [[4, 5, 6, 7], [1, 5, 9, 13]], #I-block
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], #T-block
        [[1, 5, 6, 7], [3, 5, 6, 7], [1, 2, 6, 10], [3, 2, 6, 10], [1, 5, 9, 8], [1, 5, 9, 10], [4, 5, 6, 10] [4, 5, 6, 8]], #L-block
        [[1, 2, 5, 4], [1, 5, 6, 10], [1, 2, 6, 7], [3, 6, 7, 10] ], #S-block
        [[1, 2, 5, 6]], #O-block     
    ] 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures) - 1)
        self.color = random.randint(0, (self.colors) - 1)
        self.rotation = 0
        