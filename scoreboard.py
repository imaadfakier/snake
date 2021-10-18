from turtle import Turtle

# DISPLAY_TEXT = 'S c o r e: '
DISPLAY_TEXT = 'Score: '
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

    # def __init__(self, score=0):
    def __init__(self):
        # super(Scoreboard, self).__init__()
        super().__init__()
        # self.current_high_score = 0
        with open(file='data.txt', mode='r') as file:
            self.current_high_score = int(file.read())
        # self.score = score
        self.current_score = 0
        self.hideturtle()
        self.penup()
        # self.goto(0, 250)
        # self.goto(0, 270)
        self.goto(0, 260)
        self.color('white')
        self.display_score()

    def display_score(self):
        self.clear()
        # self.write(arg=f'S c o r e = {self.score}', move=False, align='center', font=('Dubai', 16, 'bold'))
        # self.write(arg=f'S c o r e = {self.score}', move=False, align='center', font=('Dubai', 16, 'bold'))
        # self.write(arg=DISPLAY_TEXT + str(self.current_score), move=MOVE, align=ALIGNMENT, font=FONT)
        self.write(arg=DISPLAY_TEXT + str(self.current_score) + ' High Score: {high_score}'
                   .format(high_score=self.current_high_score), move=MOVE, align=ALIGNMENT, font=FONT)

    def update_score(self):
        # self.clear()
        self.current_score += 1
        self.display_score()

    # def game_has_ended(self):
    #     # self.goto(0, 0)
    #     self.home()
    #     self.write(arg='G A M E  O V E R', move=MOVE, align=ALIGNMENT, font=FONT)
    #     return True

    def reset_high_score(self):
        if self.current_score > self.current_high_score:
            self.current_high_score = self.current_score
            with open(file='data.txt', mode='w') as file:
                # file.write(str(self.current_high_score))
                # file.write('{high_score}'.format(high_score=self.current_high_score))
                file.write(f'{self.current_high_score}')
        self.current_score = 0
        self.display_score()


if __name__ == '__main__':
    print('Running scoreboard module - not main.py file')
