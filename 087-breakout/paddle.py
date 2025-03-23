import pygame
import config

class Paddle:
    def __init__(self):
        self.width = config.PADDLE_WIDTH
        self.thikness = config.PADDLE_THICKNESS
        self.color = config.PADDLE_COLOR
        
        self.reset_paddle()
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            
        if self.rect.x < 0:
            self.rect.x = 0
            
        if self.rect.x > config.WINDOW_WIDTH - self.width:
            self.rect.x = config.WINDOW_WIDTH - self.width
            

    def reset_paddle(self):
        self.speed = config.PADDLE_INITIAL_SPEED
        self.rect = pygame.Rect(
            config.WINDOW_WIDTH/2 - self.width/2,
            config.WINDOW_HEIGHT * 0.85 - self.thikness /2,
            self.width,
            self.thikness
        )
    
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
    
    