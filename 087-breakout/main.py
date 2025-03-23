# This is the entry point for the game
import pygame
import os

from game import Game

def main():
    pygame.init()
    game = Game()
    game.run()
    # pygame.quit() # this line hangs forever I don't know why 
    os._exit(0)
    

if __name__ == "__main__":
    main()