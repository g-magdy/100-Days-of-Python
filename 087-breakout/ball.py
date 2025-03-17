import pygame
import config

class Ball:
    def __init__(self):
        self.dx = config.BALL_INITIAL_SPEED
        self.dy = config.BALL_INITIAL_SPEED
        self.x =  config.WINDOW_WIDTH / 2
        self.y = config.WINDOW_HEIGHT / 2
        self.radius = config.BALL_RADIUS
        self.color = config.BALL_COLOR
    
    
    def update(self, paddle, bricks):
        # detect collision with wall
        self.detect_collision_with_walls()
        self.detect_collision_with_paddle(paddle)
        self.detect_collision_with_bricks(bricks)
        
        
        self.x += self.dx
        self.y += self.dy


    def detect_collision_with_walls(self):
        
        if self.x < self.radius:
            self.dx *= -1
        
        if self.x > config.WINDOW_WIDTH - self.radius:
            self.dx *= -1
            
        if self.y < self.radius:
            self.dy *= -1
            
        #! REMOVE THIS CONDITION IN THE FINAL GAME
        if self.y > config.WINDOW_HEIGHT - self.radius:
            self.dy *= -1

        return
    
    
    def detect_collision_with_paddle(self, paddle):
        # Check if the ball is at or below the paddle's top edge
        if self.y + self.radius > paddle.rect.y:
            # Check if the ball's x position is within the paddle's width
            if paddle.rect.x < self.x < paddle.rect.x + paddle.rect.width:
                self.dy *= -1  # Reverse vertical direction
        
    
    def detect_collision_with_bricks(self, bricks):
        pass
    
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
    