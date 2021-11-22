import numpy as np 
from headers import *

blank_arr = []

class Board:

	def __init__(self,rows,columns):
		self.__rows = rows
		self.__columns = columns
		self.grid = []
		for i in range(self.__rows):
			rows = [] 
			for j in range(self.__columns):
				rows.append(" ") 
			self.grid.append(rows)

	def get_board(self):
		# for i in range(rows):
		# 	blank_arr.append(' '*columns + '\n')
		return self.grid

	# def __init__(self,rows,columns):
	# 	self.__rows = rows
	# 	self.__columns = columns
	# 	self.grid = []
	# 	self.temp = []

	# def get_board(self):
	# 	for j in range(self.__columns):
	# 		self.temp.append(" ")
	# 	for i in range(self.__rows):
	# 	# for j in range(self.__columns):
	# 	# 	self.temp.append(" ")
	# 		self.grid.append(self.temp)

	def show_board(self):
		for i in range(self.__rows):
			for j in range(self.__columns):
				self.grid[i][j] = str(self.grid[i][j])
				# print(i)
				# print(j)
				if(self.grid[i][j] == "-"):
					print(Back.RED + self.grid[i][j], end = '')
				# else:
				# 	print(Back.LIGHTBLACK_EX + self.grid[i][j], end='')
				elif(self.grid[i][j] == "O"):
					print(Fore.GREEN + self.grid[i][j], end = '')
				elif(self.grid[i][j] == "6"):
					print(Back.WHITE + "=", end = '')
				elif(self.grid[i][j] == "4"):
					print(Back.MAGENTA + "=", end = '')
				elif(self.grid[i][j] == "2"):
					print(Back.BLUE + "=", end ='')
				# elif(self.grid[i][j] == "+"):
				# 	print(Back.WHITE + self.grid[i][j], end= '')
				else:
					print(Back.BLACK + self.grid[i][j], end='')
			print(Style.RESET_ALL, end='')
			print()