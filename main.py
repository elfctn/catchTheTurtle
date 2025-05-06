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