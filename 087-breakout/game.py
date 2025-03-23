import pygame
import config

from paddle import Paddle
from ball import Ball
from bricks import Bricks

class Game:
    
    def __init__(self):
        # this is a surface 
        # takes width, then height
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock = pygame.time.Clock()
        self.running = True
        self.lives = config.INITIAL_LIVES
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()
    
    
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)

    def display_counter(self, n):
        font = pygame.font.Font(None, 74)
        ball_dx, ball_dy = self.ball.dx, self.ball.dy  # Store current ball speed
        self.ball.dx = 0  # Stop ball movement
        self.ball.dy = 0  

        for i in range(n, 0, -1):  # Countdown from `n` to 1
            # draw a small rectangle in the middle of the screen
            pygame.rect = pygame.Rect(config.WINDOW_WIDTH / 2 - 50, config.WINDOW_HEIGHT / 2 - 50, 100, 100)
            pygame.draw.rect(self.screen, config.BACKGROUND_COLOR, pygame.rect)
            text = font.render(str(i), True, config.PADDLE_COLOR)
            text_rect = text.get_rect(center=(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2))
            self.screen.blit(text, text_rect)

            pygame.display.flip()
            
            # Use a timer instead of freezing the game
            start_time = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_time < 1000:  # Wait for 1 second
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
        
        self.ball.dx, self.ball.dy = ball_dx, ball_dy  # Restore ball speed
        

        

    def check_game_over(self):
        if (self.ball.detect_ball_miss()):
            self.lives -= 1
            self.ball.reset_ball()
            self.paddle.reset_paddle()
            self.display_counter(3)
            
        if self.lives == 0:
            self.running = False
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    
    def update(self):
        if self.running is True:
            self.paddle.update()
            self.ball.update(self.paddle, self.bricks)
            self.check_game_over()
    
    
    def draw(self):
        #! Important Line
        self.screen.fill(config.BACKGROUND_COLOR)
        
        
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.bricks.draw(self.screen)
        
        #! Important Line
        pygame.display.flip()