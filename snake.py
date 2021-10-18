from turtle import Turtle

SNAKE_SEGMENTS_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
SNAKE_MOVE_DISTANCE = 20
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class Snake:
    # '''
    # ...
    # '''
    """
    ...
    """

    # ... (ignore)
    # class attributes
    # ...

    def __init__(self):
        self.snake_segments = list()
        self.create_snake()
        self.head = self.snake_segments[-1]

    def create_snake(self):
        for position in SNAKE_SEGMENTS_POSITIONS:
            self.add_snake_segment(position)

    def move(self):
        for snake_segment in self.snake_segments[:len(self.snake_segments) - 1:]:
        # for snake_segment_index in range(0, len(self.snake_segments) - 1):
            # snake_segment.goto(
            #     self.snake_segments[self.snake_segments.index(snake_segment) + 1].xcor(),
            #     self.snake_segments[self.snake_segments.index(snake_segment) + 1].ycor()
            # )
            snake_segment.goto(
                self.snake_segments[self.snake_segments.index(snake_segment) + 1].position()
            )
            # self.snake_segments[snake_segment_index].goto(
            #     self.snake_segments[snake_segment_index + 1].position()
            # )
        self.head.forward(SNAKE_MOVE_DISTANCE)
        # print(self.snake_segments)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_snake_segment(self, position):
        turtle = Turtle(shape='square')
        turtle.penup()
        # print(position)
        turtle.goto(position)
        turtle.pensize(width=20)
        turtle.color('white')
        if len(self.snake_segments) < 3:
            self.snake_segments.append(turtle)
            return
        # else:
        self.snake_segments.insert(0, turtle)

    def extend(self):
        self.add_snake_segment(position=self.snake_segments[0].position())

    def reset_position(self):
        for snake_segment in self.snake_segments:
            # print(snake_segment)
            snake_segment.goto(700, 700)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[-1]

    # if __name__ == 'main':  # must be '__main__'
    if __name__ == '__main__':
        print('Running snake module - not main.py file')
