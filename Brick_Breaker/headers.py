import os
from colorama import Fore, init, Back, Style
init()

height = 40
max_width = 600
width = 200
start_position_x = 1
start_position_y = 40
fps = 10
t = 1/fps
rows = 50
columns = 100

normal = Style.RESET_ALL
dim = Style.DIM
red = Fore.RED