from scene import *
import math

class Point3D (object):
	def __init__(self, x = 0, y = 0, z = 0):
		self.x, self.y, self.z = float(x), float(y), float(z)

	def rotateX(self, angle):
		""" Rotates the point around the X axis by the given angle in degrees. """
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		y = self.y * cosa - self.z * sina
		z = self.y * sina + self.z * cosa
		return Point3D(self.x, y, z)

	def rotateY(self, angle):
		""" Rotates the point around the Y axis by the given angle in degrees. """
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		z = self.z * cosa - self.x * sina
		x = self.z * sina + self.x * cosa
		return Point3D(x, self.y, z)

	def rotateZ(self, angle):
		""" Rotates the point around the Z axis by the given angle in degrees. """
		rad = angle * math.pi / 180
		cosa = math.cos(rad)
		sina = math.sin(rad)
		x = self.x * cosa - self.y * sina
		y = self.x * sina + self.y * cosa
		return Point3D(x, y, self.z)

	def project(self, win_width, win_height, fov, viewer_distance):
		""" Transforms this 3D point to 2D using a perspective projection. """
		factor = fov / (viewer_distance + self.z)
		x = self.x * factor + win_width / 2
		y = -self.y * factor + win_height / 2
		return Point3D(x, y, 1)

class Simulation (Scene):
	def setup(self):

		self.screenw = 480
		self.screenh = 320

		self.vertices = [
		Point3D(-1,1,-1),
		Point3D(1,1,-1),
		Point3D(1,-1,-1),
		Point3D(-1,-1,-1),
		Point3D(-1,1,1),
		Point3D(1,1,1),
		Point3D(1,-1,1),
		Point3D(-1,-1,1)
		]

		self.faces = [(0,1,2,3),(1,5,6,2),(5,4,7,6),(4,0,3,7),(0,4,5,1),(3,2,6,7)]


		self.angleX, self.angleY, self.angleZ = 0, 0, 0

	def draw(self):

		background(0, 0, 0)

		t = []

		for v in self.vertices:
			# Rotate the point around X axis, then around Y axis, and finally around Z axis.
			r = v.rotateX(self.angleX).rotateY(self.angleY).rotateZ(self.angleZ)
			# Transform the point from 3D to 2D
			p = r.project(self.screenw, self.screenh, 256, 4)
			t.append(p)
		
		stroke(1, 1, 1)
		stroke_weight(2)
		for f in self.faces:
			line(t[f[0]].x, t[f[0]].y, t[f[1]].x, t[f[1]].y)
			line(t[f[1]].x, t[f[1]].y, t[f[2]].x, t[f[2]].y)
			line(t[f[2]].x, t[f[2]].y, t[f[3]].x, t[f[3]].y)
			line(t[f[3]].x, t[f[3]].y, t[f[0]].x, t[f[0]].y)

		self.angleX += 1
		self.angleY += 1
		self.angleZ += 1

run(Simulation(), LANDSCAPE)
