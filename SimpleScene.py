# SimpleScene module
# Provides easy use of scene module

import scene

def init(scene):
	pass
	
def width():
	return scene.self.size.w
	
def height():
	return scene.self.size.h
	
def x(value):
	if value == 1:
		return 1
	else:
		return int('0.' + str(value)
		
def y(value):
	if value == 1:
		return 1
	elif value % 2 == 0:
		return int('0.' + str(value)
	else:
		return int('0.' + str(value) + '5')

	
