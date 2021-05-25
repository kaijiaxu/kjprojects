""" A snake game coded with python, with the help of 'Programming Projects for Advanced Beginners #5: Snake' https://robertheaton.com/2018/12/02/programming-project-5-snake/
"""

import numpy
import random

class Snake(object):

    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    def take_step(self, position):
        self.body.insert(0, position)
        self.body.pop()

    def set_direction(self, direction):
        self.direction = direction

    def extend_body(self, position):
        self.body.insert(0, position)

    def head(self):
        return self.body[0]

class Apple(object):
    def __init__(self, location):
        self.location = location

class Game(object):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    INPUT_CHAR_UP = "W"
    INPUT_CHAR_LEFT = "A"
    INPUT_CHAR_DOWN = "S"
    INPUT_CHAR_RIGHT = "D"

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.snake = Snake([(5, 5), (6, 5), (7, 5), (8, 5)], self.UP)
        self.apple = Apple((3, 3))

    def render(self):
        print("Height: " + str(self.height))
        print("Width: " + str(self.width))
        board = []
        board = [[' ' for i in range(self.height)] for j in range(self.width)]

        # Print snake body and head
        for x in self.snake.body:
            board[x[0]][x[1]] = 'O'
        head = self.snake.head()
        board[head[0]][head[1]] = 'X'

        # Print apple
        apple = self.apple.location
        board[apple[0]][apple[1]] = '*'

        print(numpy.matrix(board))

    # If the snake is touching the wall, the next position will involve it passing through the wall and appearing from the opposite wall.
    def next_position(self, position, direction):
        return (
            (position[0] + direction[0]) % self.width,
            (position[1] + direction[1]) % self.height
        )

    def new_apple(self):
        while True:
            new_apple_location = (
                    random.randint(0, self.width-1),
                    random.randint(0, self.height-1),
                )
            if new_apple_location not in self.snake.body:
                break
        return new_apple_location

    def play(self):
        self.render()
        apple_count = 0
        while True:
            ch = input("").upper()

            if ch == self.INPUT_CHAR_UP and self.snake.direction != self.DOWN:
                self.snake.set_direction(self.UP)
            elif ch == self.INPUT_CHAR_DOWN and self.snake.direction != self.UP:
                self.snake.set_direction(self.DOWN)
            elif ch == self.INPUT_CHAR_LEFT and self.snake.direction != self.RIGHT:
                self.snake.set_direction(self.LEFT)
            elif ch == self.INPUT_CHAR_RIGHT and self.snake.direction != self.LEFT:
                self.snake.set_direction(self.RIGHT)

            next_position = self.next_position(self.snake.head(), self.snake.direction)
            if next_position in self.snake.body:
                break

            if next_position == self.apple.location:
                self.snake.extend_body(next_position)
                apple_count += 1
                self.apple = Apple(self.new_apple())
            else:
                self.snake.take_step(next_position)

            self.render()
        print("You lost!")
        print("Apple count: " + str(apple_count))

def main():
    game = Game(10, 20)
    game.play()

if __name__ == "__main__":
    main()
