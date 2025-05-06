import turtle
import random

screen = turtle.Screen()
screen.bgcolor('light blue')
screen.title('catch the turtle')
FONT = ('arial',30, 'normal')
score = 0
game_over = False


turtle_list = []

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle

grid_size = 10


def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color('dark blue')
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0, y)
    score_turtle.write(arg='score:0', move=False, align='center', font=FONT)
