import colorama, sys, os, math, time, copy
from colorama import Fore, Back, Style
import os
import time
import signal
import random

from getch import *
from headers import *
from board import *
from paddle import *
from ball import *
from brick import *
from lives import *

new_paddle = Paddle(6,1)
new_ball = Ball(39,1)
display = Board(rows, columns)
# lives = Lives()
display.get_board() 
new_brick1 = []
for i in range(0,10):
	new_brick1.append(Brick(i*10,10))
new_brick2 = []
for i in range(0,10):
	new_brick2.append(Brick(i*10,15))

# new_paddle.get_paddle(4)

while True:
	# display.show_board()
	# print(new_paddle.get_paddle(grid[6]))
	# display_arr = copy.deepcopy(blank_arr)
	# print("\033[H\033[J", end="")
	# display_arr = ''.join(display_arr)
	# new_ball.get_ball()
	# print(display_arr)
	# time.sleep(t)
	# os.system("clear")
	# new_paddle.move_paddle(1)
	key = input_to()
	if(key == "d"):
		new_paddle.move_paddle(4,display.get_board())
	elif(key == "a"):
		new_paddle.move_paddle(-4,display.get_board())
	elif(key == "q"):
		break
	os.system("clear")
	if(key == "z"):
		for i in range(len(new_brick1)):
			new_brick1[i].clear_brick(display.get_board())
		new_brick1 = []
		for i in range(0,10):
			new_brick1.append(Brick(i*9,11))
		for i in range(len(new_brick2)):
			new_brick2[i].clear_brick(display.get_board())
		new_brick2 = []
		for i in range(0,10):
			new_brick2.append(Brick(i*9,13))
	elif(key == "x"):
		for i in range(len(new_brick1)):
			new_brick1[i].clear_brick(display.get_board())
		new_brick1 = []
		for i in range(0,10):
			new_brick1.append(Brick(i*8,12))
		for i in range(len(new_brick2)):
			new_brick2[i].clear_brick(display.get_board())
		new_brick2 = []
		for i in range(0,10):
			new_brick2.append(Brick(i*8,14))

	new_paddle.get_paddle(display.get_board())
	new_ball.move_ball(2,display.get_board())
	if(new_ball.move_ball(2, display.get_board()) == -1):
		break
	# if(new_brick2.paddle_ball_collisions(new_paddle,new_brick2) == -1):
	# 	break
	new_ball.get_ball(display.get_board())
	# new_brick.get_brick(display.get_board())
	for i in range(0,10):
		if new_brick1[i].get_y() >= new_paddle.get_y():
			break
		new_brick1[i].get_brick(display.get_board())
		new_brick1[i].brick_ball_collisions(new_ball,display.get_board())
	for i in range(0,10):
		if new_brick2[i].get_y() >= new_paddle.get_y():
			break
		new_brick2[i].get_brick(display.get_board())
		new_brick2[i].brick_ball_collisions(new_ball, display.get_board())
	display.show_board()
	# print(new_ball.get_y)
	new_ball.paddle_ball_collisions(new_paddle, display.get_board(), new_brick1, new_brick2)
	# lives.get_lives(display.get_board())
	# lives.change_lives(display.get_board())
	# new_ball.move_ball(3)
	# new_paddle.move_paddle()
	# key = input_to()
	# if key == "a":
	# 	new_paddle

# new_paddle.move_paddle
# while true():
# 	dirn = 0
# 	key = input_to()
# 	if(key == "d"):
# 		dirn = +1
# 	if(key == "a"):
# 		dirn = -1