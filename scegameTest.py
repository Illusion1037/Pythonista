from scene import *
from scegame import *

class MyScene (Scene):
	def setup(self):
		self.touch = Touch(0, 0, 0, 0, 0)
		
		self.sprite = Sprite()
		
		self.button = Button()
		
		self.sprite.x = self.sprite.y = self.sprite.w = self.sprite.h = 24
		
		self.button.x = self.button.y = self.button.imgx = self.button.imgy = 100
		self.button.w = self.button.h = self.button.imgw = self.button.imgh = 50
		
		self.button.img = 'Typicons192_Delete'
		self.button.text = ''
		self.button.txtcolor = self.button.altbgcolor = (0, 0, 0.5)
		self.button.bgcolor = self.button.alttxtcolor = (1, 1, 1)
		
		self.sprite.type = 2
		self.sprite.load_img('ionicons-arrow-move-24')
		
		self.sprite.name = 'test'
		self.sprite.set_img('ionicons-arrow-move-24')
		
	def draw(self):
		background(1, 1, 1)
		
		self.button.draw(self.touch)
		if self.button.val == 0:
			#self.sprite.draw()
			pass
	
	def touch_began(self, touch):
		self.touch = touch
		
		self.sprite.move(touch.location[0], touch.location[1], (1, 1, 1))
	
	def touch_moved(self, touch):
		self.touch = touch
		
		self.sprite.move(touch.location[0], touch.location[1], (1, 1, 1))

	def touch_ended(self, touch):
		self.touch = Touch(0, 0, 0, 0, 0)

run(MyScene())
