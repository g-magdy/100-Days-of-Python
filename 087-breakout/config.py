# Game Constants
INITIAL_LIVES = 3

# Display constants
WINDOW_WIDTH = 760
WINDOW_HEIGHT = 880
FPS = 60
BACKGROUND_COLOR = (0, 0, 0)

# Paddle Constants
PADDLE_WIDTH = 100
PADDLE_THICKNESS = 15
PADDLE_INITIAL_SPEED = 10
PADDLE_COLOR = (255, 255, 255)

# Ball Constants
BALL_INITIAL_SPEED = 5
BALL_COLOR = (255, 255, 255)
BALL_RADIUS = 10

# Brick Constants
BRICK_WIDTH = 100
BRICK_HEIGHT = 50
BRICKS_MARGIN = 10
WALL_TO_BRICKS_MARGIN = BRICK_WIDTH + BRICKS_MARGIN
CEILING_TO_BRICKS_MARGIN = WALL_TO_BRICKS_MARGIN
BRICK_ROWS = 4
BRICK_COLUMNS = 5

# config.py

BRICK_COLORS = [
    (255, 69, 0),      # Red-Orange
    (255, 165, 0),     # Orange
    (255, 215, 0),     # Gold
    (34, 139, 34),     # Forest Green
    (0, 191, 255),     # Deep Sky Blue
    (70, 130, 180),    # Steel Blue
    (138, 43, 226),    # Blue Violet
    (220, 20, 60)      # Crimson
]
