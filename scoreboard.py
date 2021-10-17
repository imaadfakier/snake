from turtle import Turtle

DISPLAY_TEXT = 'S c o r e: '
ALIGNMENT = 'center'
MOVE = False
# FONT = ('Dubai', 24, 'normal')
# FONT = ('Courier', 24, 'normal')
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):
    # '''
    # ...
    # '''
    """
    ...
    """

    # ... (ignore)
    # class attributes
    # ...

    def __init__(self, score=0):
        # super(Scoreboard, self).__init__()
        super().__init__()
        self.score = score
        self.hideturtle()
        self.penup()
        # self.goto(0, 250)
        # self.goto(0, 270)
        self.goto(0, 260)
        self.color('white')
        self.display_score()

    def display_score(self):
        # self.write(arg=f'S c o r e = {self.score}', move=False, align='center', font=('Dubai', 16, 'bold'))
        # self.write(arg=f'S c o r e = {self.score}', move=False, align='center', font=('Dubai', 16, 'bold'))
        self.write(arg=DISPLAY_TEXT + str(self.score), move=MOVE, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_has_ended(self):
        # self.goto(0, 0)
        self.home()
        self.write(arg='G A M E  O V E R', move=MOVE, align=ALIGNMENT, font=FONT)
        return True


if __name__ == '__main__':
    print('Running scoreboard module - not main.py file')
