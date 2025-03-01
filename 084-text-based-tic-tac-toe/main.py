from tictactoe import Tictactoe

def main():
    game = Tictactoe()
    winner = None
    
    while winner is None:
        game.print_grid()
        game.move_player()
        winner = game.check_winner()

    print(f"The winner is {winner}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodBye bro👋🏼\n")