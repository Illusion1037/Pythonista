from scene import *

# -----------------------------
# scegame.py
# -----------------------------
# Module used to create
# games
# Built with the scene module
# By Noah Elazar
# -----------------------------

# Used to create backgrounds with different shapes/images
class Background ():
	def __init__(self, bglist=[], color=(1, 1, 1)):
		self.bglist = bglist
		background(color[0], color[1], color[2])
		
	def add(self, object):
		self.bglist.append(object)

# Creates a sprite
class Sprite ():
	def __init__(self, type=0, color=(0, 0, 0), x=0, y=0, w=0, h=0, img='', groups=[], name=''):
		self.type = 0
		self.color = (0, 0, 0)
		self.x = self.y = self.w = self.h = 0
		self.img = '' # For images
		self.groups = []
		#self.info = {'name':self.name, 'type':self.type, 'color':self.color, 'x':self.x, 'y':self.y, 'w':self.w, 'h':self.h, 'img':self.img}
		
	def set_pos(self, x, y):
		self.x = x
		self.y = y
		
	def get_pos(self):
		return (self.x, self.y)
	
	def resize(self, w, h):
		self.w = w
		self.h = h
		
	def get_size(self):
		return (self.w, self.h)
		
	def Rect(self):
		return Rect(x, y, w, h)
		
	def move(self, x, y, bgcolor):
		oldX = self.x
		oldY = self.y
		
		fill(bgcolor[0], bgcolor[1], bgcolor[2])
		
		if type == 0 or type == 2:
			rect(oldX, oldY, self.w, self.h)
		elif type == 1:
			ellipse(oldX, oldY, self.w, self.h)
		
		self.x = x
		self.y = y
		
	def fill(self, color):
		self.color = color
	
	def set_img(self, img):
		load_image(img)
		self.img = img
		
	def get_img(self):
		return self.img
		
	def add(self, group):
		group.add_sprite(self)
		
	def draw(self):
		
		if self.type == 0:
			fill(self.color[0], self.color[1], self.color[2])
			rect(self.x, self.y, self.w, self.h)
			
		elif self.type == 1:
			fill(self.color[0], self.color[1], self.color[2])
			ellipse(self.x, self.y, self.w, self.h)
			
		elif self.type == 2:
			image(self.img, self.x, self.y, self.w, self.h)

# Creates a group of sprites
class Group ():
	def __init__(self, spriteList=[]):
		self.spriteList = spriteList
		
	def add_sprite(self, sprite):
		if not sprite in self.spriteList:
			self.spriteList.append(sprite)
			
	def del_sprite(self, sprite):
		if sprite in self.spriteList:
			self.spriteList.remove(sprite)
			
	def get_sprites(self):
		return self.spriteList
		
	def clear(self):
		self.spriteList = []
		
	def run(self):
		for sprite in self.spriteList:
			sprite.draw()

# Creates a button
class Button ():
	def __init__(self, x=0, y=0, w=0, h=0, text='', font='Helvetica', fontsize=16, img='', imgx=0, imgy=0, imgw=0, imgh=0, txtcolor=(1, 1, 1), bgcolor=(0, 0, 0), alttxtcolor=(0, 0, 0), altbgcolor=(1, 1, 1), val=0):
		
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
		self.text = text
		self.font = font
		self.fontsize = fontsize
		
		self.img = img
		self.imgx = imgx
		self.imgy = imgy
		self.imgw = imgw
		self.imgh = imgh
		self.show_image_on_click = 1
		
		self.txtcolor = txtcolor
		self.bgcolor = bgcolor
		self.alttxtcolor = alttxtcolor
		self.altbgcolor = altbgcolor
		
		self.val = val
		
		if self.img != '':
			load_image(self.img)
		
	def add(self, menu):
		menu.add_button(self)
		
	def Rect(self):
		return Rect(self.x, self.y, self.w, self.h)
		
	def get_val(self):
		return self.val
		
	def draw(self, touch):
		
		if touch.location in Rect(self.x, self.y, self.w, self.h):
			
			self.val = 1
			
			fill(self.altbgcolor[0], self.altbgcolor[1], self.altbgcolor[2])
			
			tint(self.alttxtcolor[0], self.alttxtcolor[1], self.alttxtcolor[2])
		
		else:
			
			self.val = 0
			
			fill(self.bgcolor[0], self.bgcolor[1], self.bgcolor[2])
			
			tint(self.txtcolor[0], self.txtcolor[1], self.txtcolor[2])
		
		rect(self.x, self.y, self.w, self.h)
		
		text(self.text, self.font, self.fontsize, self.x + (self.w / 2), self.y + (self.h / 2))
		
		if not touch.location in Rect(self.x, self.y, self.w, self.h) or self.show_image_on_click:
			load_image(self.img)
			image(self.img, self.imgx, self.imgy, self.imgw, self.imgh)

# Drawing tools
class draw ():
	
	def rect(x, y, w, h, color):
		fill(color[0], color[1], color[2])
		rect(x, y, w, h)
		
	def ellipse(x, y, w, h, color):
		fill(color[0], color[1], color[2])
		ellipse(x, y, w, h)
		
	def line(pos, w, color):
		stroke(color[0], color[1], color[2])
		stroke_weight(w)
		line(pos[0], pos[1], pos[2], pos[3])

# Rectangle object
class Rectangle ():
	
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
	def set_pos(self, x, y):
		self.x = x
		self.y = y
		
	def set_size(self, w, h):
		self.w = w
		self.h = h
		
	def set_rect(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
	def get_pos(self):
		return (x, y)
		
	def get_size(self):
		return (w, h)
		
	def fill(self, type, color, img=''):
		if type == 0:
			fill(color[0], color[1], color[2])
			rect(self.x, self.y, self.w, self.h)
		elif type == 1:
			fill(color[0], color[1], color[2])
			ellipse(self.x, self.y, self.w, self.h)
		elif type == 2:
			load_image(img)
			image(img, self.x, self.y, self.w, self.h)
