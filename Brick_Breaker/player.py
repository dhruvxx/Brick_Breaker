from headers import *
import numpy as np 
import time

class Player:

	def __init__(self):
		self.__lives = 3
		self.__score = 0
		self.__stime - time.time()

	def set_score(self, score):
		self.__score = score

	def get_score(self):
		return self.__score

	def set_time(self, current_time):
		self.__stime = current_time

	def get_time(self):
		return (time.time() - self.__stime)

	def set_lives(self, lives):
		# understand your game and set this
	
	def get_lives(self):
		return self.__lives