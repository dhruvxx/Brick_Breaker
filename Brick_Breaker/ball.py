import numpy as np
import os
from headers import *
from paddle import *
from brick import *

class Ball:
	def __init__(self,height1,width1):
		self.get_x = width1
		self.get_y = height1
		self.__velocity_y = -1
		self.__velocity_x = 0
		self.__shape = "O"

	def set_x(self):
		return self.get_x

	def set_y(self):
		return self.get_y

	def set_velocity_x(self):
		return self.__velocity_x

	def set_velocity_y(self):
		return self.__velocity_y

	def update_velocity_x(self,value):
		self.__velocity_x = value

	def update_velocity_y(self,value):
		self.__velocity_y = value

	def get_ball(self,grid):
		x = self.get_x
		y = self.get_y
		grid[self.get_y][self.get_x] = self.__shape

	def erase_ball(self,grid):
		x = self.get_x
		y = self.get_y
		grid[self.get_y][self.get_x] = " "

	def move_ball(self,velocity,grid):
		r = rows
		c = columns
		if(self.get_y + self.__velocity_y >= r):
			return -1
		elif(self.get_y + self.__velocity_y < 0):
			self.__velocity_y = self.__velocity_y * (-1)
		else:
			self.erase_ball(grid)
			self.get_y = self.get_y + self.__velocity_y 

		if (self.get_x + self.__velocity_x >= c):
			self.__velocity_x = self.__velocity_x * (-1)
		elif(self.get_x + self.__velocity_x <= 0):
			self.__velocity_x = self.__velocity_x * (-1)
		else:
			self.erase_ball(grid)
			self.get_x = self.get_x + self.__velocity_x
		return 1
#ball hitting the paddle on the left of mid implies x is negative and
#hitting the paddle to the right of mid implies x is positive

	def paddle_ball_collisions(self, Paddle, grid, Brick1, Brick2):
		ball_x = self.set_x()
		ball_y = self.set_y()
		paddle_x = Paddle.get_x()
		paddle_y = Paddle.get_y()
		velocity_x = self.__velocity_x
		velocity_y = self.__velocity_y 
		if(paddle_x <= ball_x <= (paddle_x + len(Paddle.get_shape())) and paddle_y - ball_y <= 1):
			paddle_mid = paddle_x + len(Paddle.get_shape())/2
			for i in range(len(Brick1)):
				Brick1[i].clear_brick(grid)
				Brick1[i].set_y(Brick1[i].get_y() + 1)
			for i in range(len(Brick2)):
				Brick2[i].clear_brick(grid)
				Brick2[i].set_y(Brick2[i].get_y() + 1)
			if(ball_x < paddle_mid):
				velocity_x = (paddle_mid - ball_x) * (-1)
				velocity_y = self.__velocity_y * (-1)
			elif(ball_x > paddle_mid):
				velocity_x = (ball_x - paddle_x)
				velocity_y = self.__velocity_y * (-1)
			else:
				velocity_x = 0
				velocity_y = self.__velocity_y * (-1)
			os.system('mpg123 Paddle_ball_collision.mp3 &')
		self.__velocity_x = int(velocity_x)
		self.__velocity_y = int(velocity_y)
	# def wall_ball_collisions(self):
	# 	ball_x = self.set_x()
	# 	ball_y = self.set_y()
	# 	self.velocity_x = velocity_x
	# 	self.velocity_y = velocity_y
	# 	r = rows
	# 	c = columns
	# 	if(ball_x - r < 0 || ball_x - r > 0 || ball_y - c < 0 || ball_y -c > 0):
	# 		velocity_x = velocity_x * (-1)
	# 		velocity_y = velocity_y * (-1)

	