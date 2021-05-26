"""Conway’s Game of Life using Python, based on "Programming Projects for Advanced Beginners #2: Game of Life" https://robertheaton.com/2018/07/20/project-2-game-of-life/
"""
import random
import numpy as np

class state(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def render(self):
        board_state = [[" " for i in range(self.height)] for j in range(self.width)]
        # Random state: randomize each element of `state` to either 0 or 1
        for x, row in enumerate(board_state):
            for y, col in enumerate(row):
                random_number = random.random()
                # We can change the probability to get a board state with more or less live cells
                if random_number >= 0.5:
                    board_state[x][y] = " "
                else:
                    board_state[x][y] = "*"
        # Pretty print board
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board_state]))
        # Loop forever
        while True:
            self.next_board_state(board_state)

    def next_board_state(self, board_state):
        """
        1. Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
        2. Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
        3. Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
        4. Any dead cell with exactly 3 live neighbors becomes alive, by reproduction
        """
        # Find number of live neighbours
        new_board = np.pad(board_state, pad_width=1, mode='constant', constant_values=" ")
        dimensions = np.shape(board_state)
        neighbours = [[0 for i in range(self.height)] for j in range(self.width)]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                live_neighbours = 0
                for k in range(3):
                    if new_board[i][j + k] == "*":
                        live_neighbours += 1
                    if new_board[i + 2][j + k] == "*":
                        live_neighbours += 1
                if new_board[i + 1][j] == "*":
                    live_neighbours += 1
                if new_board[i + 1][j + 2] == "*":
                    live_neighbours += 1
                neighbours[i][j] = live_neighbours

        temp = [[" " for i in range(self.height)] for j in range(self.width)]
        for i in range(dimensions[0]):
            for j in range(dimensions[1]):
                # Any live cell with 0 or 1 live neighbors becomes dead
                if (neighbours[i][j] == 0 or neighbours[i][j] == 1) and board_state[i][j] == "*":
                    temp[i][j] = " "
                # Any live cell with 2 or 3 live neighbors stays alive
                if (neighbours[i][j] == 2 or neighbours[i][j] == 3) and board_state[i][j] == "*":
                    temp[i][j] = "*"
                # Any live cell with more than 3 live neighbors becomes dead
                if neighbours[i][j] > 3 and board_state[i][j] == "*":
                    temp[i][j] = " "
                # Any dead cell with exactly 3 live neighbors becomes alive
                if neighbours[i][j] == 3 and board_state[i][j] == " ":
                    temp[i][j] = "*"
        board_state = temp.copy()
        print("______________________________________")
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in board_state]))

def main():
    # We can change the width and height as we wish
    width = 5
    height = 5
    life = state(width, height)
    life.render()

if __name__ == "__main__":
    main()
