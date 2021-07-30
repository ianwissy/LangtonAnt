# Ian Wyse
# 7/20/2021
# Contains a simulation of Langston's Ant.

class Ant:
    """Object class for Langston's ant simulation. Class contains an initialization method for new ant objects,
    a run_simulation method which runs a Langston's ant simulation using _make_board to make an initial bord to
    run the simulation on, _white_move to move the ant if it is on a white square, and _black_move to move it if it
    is on a black square. Also contains a print_board method used to print out a given board state in the console."""

    def __init__(self, size, row, column, orientation):
        """"""
        self._size = size
        self._row = row
        self._column = column
        self._orientation = orientation

    def _make_board(self):
        """Initializes and returns a self._size by self._size matrix of all white squares."""
        mat = []
        for m in range(self._size):
            column = []
            for n in range(self._size):
                column.append("_")
            mat.append(column)
        return mat

    def print_board(self, mat):
        """Prints out the board state associated with a given matrix after placing the ant in its current location."""
        mat[self._row][self._column] = "8"
        for i in range(len(mat)):
            string = ""
            for j in range(len(mat)):
                string += mat[i][j]
            print(string)

    def _white_move(self, mat):
        """Turns the ant right and moves it forward. Also updates the given board matrix and the ant's
        properties to reflect that move."""
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

    def _black_move(self, mat):
        """Turns the ant left and then moves it forward. Also updates the given board matrix and the ant's
        properties to reflect that move."""
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
        """Takes in a number of steps and runs a Langston's Ant simulation for that number of moves using the Ant's
        current position, orientation, and board size sata. Returns the board matrix
        for the endpoint of the simulation."""
        mat = self._make_board()
        for i in range(steps):
            if mat[self._row][self._column] == "_":
                self._white_move(mat)
            else:
                self._black_move(mat)
        return mat


def main():
    """Requests board size, starting location, and and orientation information from the user, then initializes an
    Ant object using that information. Next, the function requests a number of steps, then runs a Langston's Ant
    simulation based on the information given, printing out a board state associated with the final state of the
    board after the simulation has run. In this board, white squares are represented by "_", black squares are
    represented by "#", and the ant is represented by "8"."""
    print("Welcome to Langton's ant simulation!")
    print("First, please enter a number no larger than 100 for the size of the square board:")
    size = int(input())
    print("Choose the ant’s starting location, please enter a number as the starting row number (where 0 is the first "
          "row from the top):")
    row = int(input())
    print("Please enter a number as the starting column number (where 0 is the first column from the left):")
    column = int(input())
    print("Please choose the ant’s starting orientation, 0 for up, 1 for right, 2 for down, 3 for left:")
    orientation = int(input())
    ant = Ant(size, row, column, orientation)
    print("Please enter the number of steps for the simulation:")
    steps = int(input())
    mat = ant.run_simulation(steps)
    ant.print_board(mat)
