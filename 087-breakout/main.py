# This is the entry point for the game
import pygame
import os

from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    print("Reached here")
    # pygame.quit()
    print("Reached there")
    os._exit(0)
    

if __name__ == "__main__":
    main()