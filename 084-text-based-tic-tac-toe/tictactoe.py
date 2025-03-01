import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Tictactoe:
    def __init__(self):
        self.grid = [['' for _ in range(3)] for _ in range(3)]
        self.player1_sign = 'X'
        self.player2_sign = 'O'
        self.current_turn = 0
    
    
    def print_grid(self):
        clear_screen()
        for i in range(3):
            for j in range(3):
                print(f" {self.grid[i][j] if self.grid[i][j] != '' else " "} ", end="")
                print('|' if j != 2 else '\n', end="")
            print("-----------" if i != 2 else '')
    
    def __get_valid_int(self, current_player_sign, row_or_col):
        while True:
            try:
                num = int(input(f"Put {current_player_sign} in which {row_or_col}? "))
                if num >= 1 and num <= 3:
                    return num - 1
                else:
                    print(f"invalid {row_or_col} number")
            except ValueError:
                print("invalid data was given")


    def __get_valid_position(self, current_player_sign):
        while True:
            chosen_i = self.__get_valid_int(current_player_sign, "row")
            chosen_j = self.__get_valid_int(current_player_sign, "column")
            if self.grid[chosen_i][chosen_j] != "":
                print("this position is taken by the other player, try again")
            else:
                return chosen_i, chosen_j


    def move_player(self):
        current_player_sign = self.player1_sign if self.current_turn == 0 else self.player2_sign
        print(f"It is Player {self.current_turn + 1}'s Turn")        
        row, column = self.__get_valid_position(current_player_sign)
        self.grid[row][column] = current_player_sign
        self.current_turn = 1 - self.current_turn
    
    
    def check_winner(self):
        for i in range(3):
            # horizontal check
            if (self.grid[i][0] == self.grid[i][1] == self.grid[i][2]) and self.grid[i][0] in ["X", "O"]:
                return self.grid[i][0]
            # vertical check
            if (self.grid[0][i] == self.grid[1][i] == self.grid[2][i]) and self.grid[0][i] in ["X", "O"]:
                return self.grid[0][i]
        
        # check two diagonals
        if (self.grid[0][0] == self.grid[1][1] == self.grid[2][2]) and self.grid[0][0] in ["X", "O"]:
            return self.grid[0][0]
        if (self.grid[0][2] == self.grid[1][1] == self.grid[2][0]) and self.grid[0][2] in ["X", "O"]:
            return self.grid[1][1]
        
        return None