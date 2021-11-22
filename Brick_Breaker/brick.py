import numpy as np
from headers import *

class Brick:
	def __init__(self,x,y):
		score = 0
		self.__score = score 
		self.__x = x
		self.__y = y 
		self.__width = 7
		self.__height = height
		self.__shape = "======="
		self.__strength = 6
		self.__velocity_y = -2
		self.__velocity_x = 0

	# b1 = Brick(x,y)
	# b2 = Brick(x,y)

	def get_x(self):
		return self.__x

	def get_y(self):
		return self.__y

	def set_x(self,x):
		self.__x = x

	def set_y(self,y):
		self.__y = y

	def change_Score(self,value):
		self.__score = score + value

	def get_lives(self):
		return self.__lives

	def get_score(self):
		return self.__score

	def change_lives(self):
		self.__lives = self.__lives - 1

	def get_shape(self):
		return self.__shape

	#get brick of three different colours each with different strengths

	def get_brick(self,grid):
		if(self.__x == "NONE" and self.__y == "NONE"):
			return 
		x = self.__x
		y = self.__y
		w = len(self.get_shape())
		for i in range(x,x+w):
			grid[self.__y][i] = self.__shape[i-x]
		return grid

	def erase_brick(self,grid):
		if(self.__x == "NONE" and self.__y == "NONE"):
			return 
		x = self.__x
		y = self.__y
		w = len(self.get_shape())
		h = self.__height
		if(self.__strength == 0):
			for i in range(x, x+w):
				grid[self.__y][i] = " "
		self.__x = "NONE"
		self.__y = "NONE"

	def clear_brick(self,grid):
		x = self.__x
		y = self.__y
		w = len(self.get_shape())
		for i in range(x, x+w):
			grid[self.__y][i] = " "
		del self

	def brick_color(self,grid):
		if(self.__x == "NONE" and self.__y == "NONE"):
			return 
		# if(self.__strength == 2):
		# 	self.color = Fore.BLUE
		# elif(self.__strength == 0):
		# 	self.color = Fore.GREEN
		# else:
		# 	self.color = Fore.MAGENTA
		x = self.__x
		y = self.__y
		w = len(self.get_shape())
		for i in range(x,x+w):
			grid[self.__y][i] = self.__strength
		return grid

	def brick_ball_collisions(self, Ball, grid):
		if(self.__x == "NONE" and self.__y == "NONE"):
			return 
		ball_x = Ball.set_x()
		ball_y = Ball.set_y()
		brick_x = self.__x
		brick_y = self.__y
		w = self.__width
		length = len(self.get_shape())
		velocity_x = Ball.set_velocity_x()
		velocity_y = Ball.set_velocity_y()
		# if(brick_x <= ball_x and ball_x <= (brick_x + len(self.get_shape())) and brick_y - ball_y <= 1):
		# 	brick_mid = brick_x + len(self.get_shape())/2
		# 	if(ball_x < brick_mid):
		# 		velocity_x = brick_mid - ball_x
		# 		velocity_y = self.__velocity_y * (-1)
		# 		self.__strength = self.__strength - 2
		# 	elif(ball_x > brick_mid):
		# 		velocity_x = (ball_x - brick_x) * (-1)
		# 		velocity_y = self.__velocity_y * (-1)
		# 		self.__strength = self.__strength - 2
		# 	else:
		# 		velocity_x = 0
		# 		velocity_y = self.__velocity_y * (-1)
		# 		self.__strength = self.__strength - 2

		if(brick_x < ball_x and ball_x < (brick_x + length)):
			if(abs(ball_y - brick_y) <= 1):
				velocity_y = self.__velocity_y * (-1)
				self.__strength = self.__strength - 2
				os.system('mpg123 Brick_ball_collision.mp3 &')


		elif(brick_y > ball_y and ball_y > (brick_y - w)):
			if(abs(ball_x - brick_x) <= 1):
				velocity_x = self.__velocity_x * (-1)
				self.__strength -= 2
				os.system('mpg123 Brick_ball_collision.mp3 &')

		Ball.update_velocity_x(velocity_x)
		Ball.update_velocity_y(velocity_y)
		self.brick_color(grid)

		if(self.__strength <= 0):
			self.erase_brick(grid)