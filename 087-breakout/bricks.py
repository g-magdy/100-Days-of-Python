import pygame
import config
import random

class Brick:
    def __init__(self, x_top_left, y_top_left, color):
        self.color = color
        self.rect = pygame.Rect(
            x_top_left,
            y_top_left,
            config.BRICK_WIDTH,
            config.BRICK_HEIGHT
        )
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=4)

class Bricks:
    def __init__(self):
        self.reset_bricks()
    
    def reset_bricks(self):
        self.bricks = []
        y = config.WINDOW_HEIGHT * 0.1  # 10% of the window height
        for i in range(config.BRICK_ROWS):
            
            x = (config.WINDOW_WIDTH - (config.BRICK_COLUMNS * (config.BRICK_WIDTH + config.BRICKS_MARGIN))) / 2
            for j in range(config.BRICK_COLUMNS):
                b = Brick(x, y, random.choice(config.BRICK_COLORS))
                self.bricks.append(b)
                x = x + config.BRICK_WIDTH + config.BRICKS_MARGIN
            
            y = y + config.BRICK_HEIGHT + config.BRICKS_MARGIN
        
        
    def draw(self, screen):
        for brick in self.bricks:
            brick.draw(screen)
    
    def update(self):
        pass