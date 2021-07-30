#Ian Wyse
#7/20/2021
#Contains a simulation of Langston's Ant.

class Ant:
    """"""

    def __init__(self, size, row, column, orientation):
        """"""
        self._size = size
        self._row = row
        self._column = column
        self._orientation = orientation

    def make_board(self):
        """"""
        mat = []
        for m in range(self._size):
            column = []
            for n in range(self._size):
                column.append("_")
            mat.append(column)
        return mat

    def print_board(self, mat):
        mat[self._row][self._column] = "8"
        for i in range(len(mat)):
            string = ""
            for j in range(len(mat)):
                string += mat[i][j]
            print(string)

    def white_move(self, mat):
        self._orientation = (self._orientation + 1) % 4
        mat[self._row][self._column] = "#"
        if self._orientation == 0:
            self._row = (self._row - 1) % self._size
        elif self._orientation == 1:
            self._column = (self._column + 1) % self._size
        elif self._orientation == 2:
            self._row = (self._row + 1) % self._size
        elif self._orientation == 3:
            self._column = (self._column - 1) % self._size

    def black_move(self, mat):
        self._orientation = (self._orientation - 1) % 4
        mat[self._row][self._column] = "_"
        if self._orientation == 0:
            self._row = (self._row - 1) % self._size
        elif self._orientation == 1:
            self._column = (self._column + 1) % self._size
        elif self._orientation == 2:
            self._row = (self._row + 1) % self._size
        elif self._orientation == 3:
            self._column = (self._column - 1) % self._size

    def run_simulation(self, steps):
        """"""
        mat = self.make_board()
        for i in range(steps):
            if mat[self._row][self._column] == "_":
                self.white_move(mat)
            else:
                self.black_move(mat)
        self.print_board(mat)


def main():
    """"""
    print("Welcome to Langton's ant simulation!")
    print("First, please enter a number no larger than 100 for the size of the square board:")
    size = int(input())
    print("Choose the ant’s starting location, please enter a number as the starting row number (where 0 is the first row from the top):")
    row = int(input())
    print("Please enter a number as the starting column number (where 0 is the first column from the left):")
    column = int(input())
    print("Please choose the ant’s starting orientation, 0 for up, 1 for right, 2 for down, 3 for left:")
    orientation = int(input())
    ant = Ant(size, row, column, orientation)
    print("Please enter the number of steps for the simulation:")
    steps = int(input())
    ant.run_simulation(steps)

main()