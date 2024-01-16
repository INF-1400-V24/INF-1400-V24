from board import Board
from square import Square

class TicTacBoard(Board):

    def __init__(self):
        startup_list = [[None for _ in range(9)] for _ in range(9)]
        super().__init__(startup_list)
        self._set_up_nums()

    def _set_up_nums(self):
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.nums[i][j] = Square()

    def play(self):
        current_player = 1
        x, y = -1, -1
        while not self.check_winner():
            print()
            print(self)
            print("It's player", current_player, "'s turn")
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            placed = self.place_piece(current_player, x, y)
            if not placed:
                print("Already taken, try again")
            else:
                print("Next player!")
                current_player = 2 if current_player == 1 else 1
        winner = self.check_winner()
        print("The winner is", winner)

    def place_piece(self, player, x, y):
        return self.nums[x][y].change_num(player)

    def check_winner(self):
        for row in self.nums:
            row_numbers = [sq.player for sq in row]
            if row_numbers.count(1) == self.n_cols:
                return True, 1
            elif row_numbers.count(2) == self.n_cols:
                return True, 2
        for i in range(self.n_rows):
            col_numbers = []
            for j in range(self.n_cols):
                col_numbers.append(self.nums[j][i].player)
            if col_numbers.count(1) == self.n_cols:
                return True, 1
            elif col_numbers.count(2) == self.n_cols:
                return True, 2
        return False
            


if __name__ == "__main__":
    tt = TicTacBoard()
    tt.play()
    print(tt)