import pygame
import config
import math


class Ball:
    def __init__(self):
        self.reset_ball()
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

    def reset_ball(self):
        self.dx = config.BALL_INITIAL_SPEED
        self.dy = config.BALL_INITIAL_SPEED
        self.x =  config.WINDOW_WIDTH / 2
        self.y = config.WINDOW_HEIGHT / 2
    
    
    def detect_ball_miss(self):
        if self.y > config.WINDOW_HEIGHT - self.radius:
            return True
        else:
            return False


    
    
    def detect_collision_with_paddle(self, paddle):
        next_x = self.x + self.dx
        next_y = self.y + self.dy

        # Check if the ball will hit the paddle
        if next_y + self.radius >= paddle.rect.y and self.y < paddle.rect.y:
            if paddle.rect.x <= next_x <= paddle.rect.x + paddle.rect.width:
                self.dy *= -1  # Reverse vertical direction

                # Prevent sticking by placing the ball just above the paddle
                self.y = paddle.rect.y - self.radius  

                # Compute bounce angle based on where the ball hit the paddle
                hit_position = (self.x - paddle.rect.x) / paddle.rect.width  # 0 (left) → 1 (right)
                max_bounce_angle = math.radians(60)  # Max deviation ±60°

                bounce_angle = (hit_position - 0.5) * 2 * max_bounce_angle  # Convert to angle

                # Maintain ball speed
                speed = math.hypot(self.dx, self.dy)
                self.dx = speed * math.sin(bounce_angle)
                self.dy = -speed * math.cos(bounce_angle)  # Always bounce upward




    
    def detect_collision_with_bricks(self, bricks):
        for brick in bricks.bricks:
            if self.x + self.radius > brick.rect.left and self.x - self.radius < brick.rect.right:
                if self.y + self.radius > brick.rect.top and self.y - self.radius < brick.rect.bottom:
                    # Determine which side the ball hit
                    if abs(self.x - brick.rect.left) < self.radius or abs(self.x - brick.rect.right) < self.radius:
                        self.dx *= -1  # Bounce horizontally
                    else:
                        self.dy *= -1  # Bounce vertically

                    # Remove the brick
                    bricks.bricks.remove(brick)
                    return  # Avoid multiple removals per frame


    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
    