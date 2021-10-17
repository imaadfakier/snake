# from turtle import Screen, Turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('The Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.display_score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_over = False

# while True:
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect food collision
    # if snake.head.distance(food) < 15:
    if snake.head.distance(food) < 13:
        # print('food collision detected!')
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    # detect wall collision
    if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or (snake.head.ycor() > 290) or (snake.head.ycor() < -290):
        game_over = scoreboard.game_has_ended()

    # detect tail collision
    # if head collides with any segment in the tail:
        # trigger game_has_ended()
    for snake_segment in snake.snake_segments[:len(snake.snake_segments) - 1:]:  # slicing; [start:up to but not includi
                                                                                 # -ng:increment]
        if snake.head.distance(snake_segment) < 10:
            game_over = scoreboard.game_has_ended()

screen.exitonclick()

# tuple slicing
# piano_tuple = ('do', 're', 'me', 'fa', 'so', 'la', 'ti')
# print(piano_tuple)
# print(piano_tuple[2:5])  # will return ('me', 'fa', 'so')
# print(piano_tuple[1:])  # will return ('re', 'me', 'fa', 'so', 'la', 'ti')
