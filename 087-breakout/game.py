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
        self.start_time = pygame.time.get_ticks()
        self.running = True
        self.lives = config.INITIAL_LIVES
        self.paddle = Paddle()
        self.ball = Ball()
        self.bricks = Bricks()
    
    def draw_hub(self):
        font = pygame.font.Font(None, 36)  

        # Display Lives
        lives_text = font.render(f'Lives: {self.lives}', True, (255, 255, 255))
        self.screen.blit(lives_text, (20, 10))  # Position near the top-left

        # Display Timer
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000  # Convert ms to seconds
        timer_text = font.render(f'Time: {elapsed_time}s', True, (255, 255, 255))
        self.screen.blit(timer_text, (config.WINDOW_WIDTH - 120, 10))  # Position near top-right
    
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
            if self.lives == 0:
                self.game_over_screen()
            else:
                self.display_counter(3)
            
    
    def game_over_screen(self):
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over\nPress Enter to Play again\nPress Escape To Exit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(config.WINDOW_WIDTH / 2, config.WINDOW_HEIGHT / 2))

        self.screen.fill((0, 0, 0))  # Clear screen
        self.screen.blit(text, text_rect)

        pygame.display.flip()  # Update display

        while True:  # Wait for valid key press
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Restart game
                        self.lives = config.INITIAL_LIVES
                        self.start_time = pygame.time.get_ticks()
                        self.ball.reset_ball()
                        self.paddle.reset_paddle()
                        self.bricks.reset_bricks()
                        self.display_counter(3)
                        return  # Exit game over screen
                    elif event.key == pygame.K_ESCAPE:  # Quit game
                        self.running = False
                        return

    
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
        
        self.draw_hub()
        self.paddle.draw(self.screen)
        self.ball.draw(self.screen)
        self.bricks.draw(self.screen)
        
        #! Important Line
        pygame.display.flip()