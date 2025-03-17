import pygame
import config

from paddle import Paddle
from ball import Ball

class Game:
    
    def __init__(self):
        # this is a surface 
        # takes width, then height
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = None
    
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)

    
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    
    def update(self):
        if self.running is True:
            print("Start Updade")
            self.paddle.update()
            self.ball.update(self.paddle, self.bricks)
            print("Finish")
    
    
    def draw(self):
        #! Important Line
        self.screen.fill(config.BACKGROUND_COLOR)
        
        
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        
        #! Important Line
        pygame.display.flip()