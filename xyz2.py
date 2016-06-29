from scene import *
from cmath import sin, cos

class Test (Scene):
	def setup(self):
		pass
		
	def xy(self, x, y, z, rcx=0, rcy=0, rcz=0, rx=0, ry=0, rz=0, camx=0, camy=0, camz=0, fs=480):
		newx = (((((x - rcx) * cos(ry)) - ((z-rcz) * sin(ry))) * cos(rz)) - (((((y - rcy) * cos(rx)) - (((x - rcx) * sin(ry)) + (z - rcz) * cos(ry)) * sin(rx)) * sin(rz)) - camx) * (fs / (fs + ((((y - rcy) * sin(rx) + ((((x-rcx) * sin(ry)) + ((z - rcz) * cos(ry)) * cos(rx)) - camz)
		
		newy = (((((x - rcx) * cos(ry)) - ((z-rcz) * sin(ry))) * cos(rz)) - (((((y - rcy) * cos(rx)) - (((x - rcx) * sin(ry)) + (z - rcz) * cos(ry)) * sin(rx)) * sin(rz)) - camy) * (fs / (fs + ((((y - rcy) * sin(rx) + ((((x-rcx) * sin(ry)) + ((z - rcz) * cos(ry)) * cos(rx)) - camz)                                                                                                                                                                           
		
		return newx, newy
	
	def draw(self):
		background(0, 0, 0)
		stroke(0, 0, 1)
		stroke_weight(2)
		
		line(self.xy(50, 50, 50)[0], self.xy(50, 50, 50)[1], self.xy(50, 50, 0)[0], self.xy(50, 50, 0)[1])
		
		print(self.xy(50, 50, 50)[0], self.xy(50, 50, 50)[1], self.xy(50, 50, 0)[0], self.xy(50, 50, 0)[1])
		
run(Test())
