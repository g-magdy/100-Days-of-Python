import pygame
import config

class Game:
    
    def __init__(self):
        # this is a surface 
        # takes width, then height
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True
    
    
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
        pass
    
    
    def draw(self):
        pass