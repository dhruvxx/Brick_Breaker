# paddle = "|===|========|===|"

import numpy as np 
from headers import *
# from board import *

class Paddle:

	def __init__(self,width,height=1):
		self.__x = start_position_x
		self.__y = start_position_y
		# self.__v = 1
		self.__width = 5 
		self.__height = height 
		self.__shape = "-----"
		# self.grid = []
		# self.__move = move
		# self.__paddle = "|===|========|===|"
		# self.__paddle = []
		# self.__empty = "|===|========|===|"
		# self.__empty = []

		# self.__lives = 3
		# score = 0
		# self.__score = score 

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def set_x(self,x):
		self.__x = x

	def set_y(self,y):
		self.__y = y

	def get_shape(self):
		return self.__shape

	def get_paddle(self,grid):
		x = self.__x
		y = self.__y
		h = self.__height
		w = self.__width 
		for i in range(x,x+w):
			# print("hey")
			# grid[i] = paddle(i-y)
			grid[self.__y][i] = self.__shape[i-x]
		return grid
# grid[self.__y][i] + color + symbol*w + Fore.RESET + Back.RESET
	def erase_paddle(self,grid):
		x = self.__x
		y = self.__y
		w = self.__width
		h = self.__height
		for i in range(x, x+w):
			grid[self.__y][i] = " "

	def move_paddle(self, velocity, grid):
		# self.erase_paddle(grid)
		c = columns
		w = self.__width
		if (self.__x + velocity + w >= c):
			return
		elif(self.__x + velocity <= 0):
			return
		else:
			self.erase_paddle(grid)
			self.__x = self.__x + velocity
			# self.get_paddle(Back.RED, ' ', display_arr)
		# current_y = y-3
		# if(current_y<3):
		# 	current_y = 3
		# if(self.__x <= 0 and dirn == -1):
		# 	return
		# if(self.__x + width >= columns):
		# 	return

		# self.set_y(current_y)
		# self.get_paddle(grid)

# move, render, clear, get

# render ball, move ball 

# initialize, change life, brick ball collision and render brick - brick