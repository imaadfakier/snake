from turtle import Turtle
from random import randint


class Food(Turtle):
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
        # super(Food, self).__init__()
        super().__init__()
        self.shape(name='circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # halving default shape size;
                                                          # default size is 20 x 20
        self.color('blue')
        self.refresh()

    def refresh(self):
        self.speed(speed='fastest')
        self.goto(x=randint(-280, 280), y=randint(-280, 280))


if __name__ == '__main__':
    print('Running food module - not main.py file')
