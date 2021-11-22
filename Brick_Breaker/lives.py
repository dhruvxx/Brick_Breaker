import numpy as np
from headers import *
from ball import *

class Lives:
	def __init__(self):
		self.__x = 5
		self.__y = 10
		self.__lives = 3

	def get_lives(self,grid):
		x = self.__x
		for i in range(x,x+self.__lives):
			grid[self.__y][i] = "+"
		return grid

	def change_lives(self,grid):
		Ball_y = Ball.get_y()
		if(Ball_y + Ball.set_velocity_y(self) >= r):
			self.__lives -= 1