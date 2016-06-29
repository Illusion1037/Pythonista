from scene import *

black =		(0, 0, 0, 1)
grey =		(0.5, 0.5, 0.5, 1)
white =		(1, 1, 1, 1)
red =		(1, 0, 0, 1)
green =		(0, 1, 0, 1)
blue =		(0, 0, 1, 1)
yellow =	(1, 1, 0, 1)
cyan =		(0, 1, 1, 1)
violet =	(1, 0, 1, 1)
orange =	(1, 0.5, 0, 1)

def set(color):
	fill(*color)
	tint(*color)
	stroke(*color)
