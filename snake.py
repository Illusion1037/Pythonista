from scene import *
import time
import random

class Snake (Scene):
	def setup(self):
		self.red = 		Color(1, 0, 0)
		self.black = 	Color(0, 0, 0)
		self.white = 	Color(1, 1, 1)
		self.grey = 		Color(0.5, 0.5, 0.5)
		
		self.snakePos = [100, 100]
		self.snakeSegs = [[100, 100], [80, 100], [60, 100]]
		
		self.rasPos = [300, 220]
		self.rasSpawned = 1
		
		self.dir = 'right'
		self.changeDir = self.dir
		
		self.gameover = False
		
		self.score = 0
		self.highscore = self.gethighscore()
		
		self.touchdown = 0
		self.touchup = 0
		self.menuhide = 0
		self.startcontrol = 0
		
	def gameOver(self):
		tint(self.grey.r, self.grey.g, self.grey.b)
		text('Game Over', 'AvenirNext-Regular', 72, 240, 180)
		self.gameover = True
	
	def menu(self):
		fill(0, 0, 0)
		rect(0, 0, 480, 320)
		tint(self.white.r, self.white.g, self.white.b)
		text('S N A K E', 'DejaVuSansMono-Bold', 72, 240, 160)
		
		text('tap to play', 'AvenirNext-Regular', 16, 240, 5, 8)
		
	def gethighscore(self):
		f = open('snake_highscore.txt', 'r')
		highscore = f.read()
		f.close()
		
		return highscore
		
	def sethighscore(self, score):
		f = open('snake_highscore.txt', 'w')
		f.write(str(score))
		f.close()
	
	def main(self):
		if not self.gameover:
			time.sleep(0.2)
		
		if self.changeDir == 'right' and not self.dir == 'left':
			self.dir = self.changeDir
		if self.changeDir == 'left' and not self.dir == 'right':
			self.dir = self.changeDir
		if self.changeDir == 'up' and not self.dir == 'down':
			self.dir = self.changeDir
		if self.changeDir == 'down' and not self.dir == 'up':
			self.dir = self.changeDir
		
		if self.dir == 'right':
			self.snakePos[0] += 20
		if self.dir == 'left':
			self.snakePos[0] -= 20
		if self.dir == 'up':
			self.snakePos[1] += 20
		if self.dir == 'down':
			self.snakePos[1] -= 20
		
		self.snakeSegs.insert(0, list(self.snakePos))
		
		if self.snakePos == self.rasPos:
			self.rasSpawned = 0
			self.score += 1
		else:
			self.snakeSegs.pop()
			
		if self.rasSpawned == 0:
			x = random.randrange(1, 24)
			y = random.randrange(1, 16)
			self.rasPos = [int(x*20), int(y*20)]
		self.rasSpawned = 1
		
		background(self.black.r, self.black.g, self.black.b)
		
		if self.gameover == False:
			fill(self.white.r, self.white.g, self.white.b)
			for pos in self.snakeSegs:
				ellipse(pos[0], pos[1], 20, 20)
			
			fill(self.red.r, self.red.g, self.red.b)
			rect(self.rasPos[0], self.rasPos[1], 20, 20)
		
		tint(self.grey.r, self.grey.g, self.grey.b)
		if not self.gameover:
			text(str(self.score), 'AvenirNext-Regular', 16, 5, 315, 3)
		else:
			text('Score: ' + str(self.score), 'AvenirNext-Regular', 16, 240, 130)
			
			if self.score > int(self.highscore):
				self.sethighscore(self.score)
				text('New Highscore!', 'AvenirNext-Regular', 16, 240, 110)
			else:
				text('Highscore: ' + self.highscore, 'AvenirNext-Regular', 16, 240, 110)
				
		if self.snakePos[0] > 460 or self.snakePos[0] < 0:
			self.gameOver()
		if self.snakePos[1] > 300 or self.snakePos[1] < 0:
			self.gameOver()
		for seg in self.snakeSegs[1:]:
			if self.snakePos == seg:
				self.gameOver()
		
		if self.startcontrol != 2:
			self.startcontrol += 1
					
	def draw(self):
		if not self.menuhide:
			self.menu()
		else: 
			self.main()
		if self.touchup:
			self.menuhide = 1
		if self.gameover == 1:
			self.gameOver()
			#time.sleep(1)
			if self.touchup:
				#time.sleep(1)
				self.setup()
		
		if self.touchup:
			self.touchup = 0
	
	def touch_began(self, touch):
		self.touchdown = 1
	
	def touch_moved(self, touch):
		pass

	def touch_ended(self, touch):
		if self.startcontrol == 2:
			if touch.location.x > 320:
				self.changeDir = 'right'
			elif touch.location.x < 160:
				self.changeDir = 'left'
			elif touch.location.y > 160:
				self.changeDir = 'up'
			else:
				self.changeDir = 'down'
		#self.touchdown = 0
		self.touchup = 1

run(Snake(), LANDSCAPE)
