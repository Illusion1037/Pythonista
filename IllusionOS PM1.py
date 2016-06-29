#coding: utf-8

# An imitation OS made with the scene module
# by Noah Elazar

from scene import *
from math import floor
from datetime import datetime

class os (Scene):
	
	def setup(self):
		
		# Screensize
		screensize = (480, 320)
		
		# Define variables
		self.repeat = 1
		
		# Current app
		self.app = 'home'
		
		# Num of apps
		self.num_apps = 5
		
		# Applinks drawn
		self.apps_drawn = 0
		
		# Set to current touch
		self.Touch = Touch(-100, -100, -100, -100, 0)
		
		self.pendingTouch = Touch(-100, -100, -100, -100, 0)
		
		# Set to pressed button
		self.button_down = ''
		
		# Set to all selected check boxes
		self.chckbx_true = []
		
		# Set to current popup
		self.popup = ''
	
	def draw(self):
		
		# Returns the current time as a list
		def curr_time():
			
			# Current time
			timelist = str(datetime.now()).split()
			time = timelist[1]
			
			# Breaks up str of current time
			hour = int(time[0:2])
			min = int(time[3:5])
			sec = int(time[6:8])
			
			# If it is noon or later
			if hour >= 12:
				
				# If it is 12 midnight
				if hour == 24:
					am_pm = 'am'
				else:
					am_pm = 'pm'
			
			else: # Before noon
				am_pm = 'am'
			
			# Convert to 12 hour time	
			if hour > 12:
				hour -= 12
			
			# Add zero to front of numbers
			if hour < 10:
				hour = '0' + str(hour)
			else:
				hour = str(hour)
			
			if min < 10:
				min = '0' + str(min)
			else:
				min = str(min)
			
			if sec < 10:
				sec = '0' + str(sec)
			else:
				sec = str(sec)
			
			# Convert to list
			timelist = [hour, min, sec, am_pm]
			
			# Return list
			return timelist
		
		# New background, can be used in or as an app
		def new_bg(name, color=(1, 1, 1), show_x_button=True):
			
			# Colors the background
			background(color[0], color[1], color[2])
			
			# Draws rect with title
			draw_rect(0, 420, 320, 60, (0, 0, 0))
			tint(1, 1, 1)
			text(name, 'AvenirNext-Regular', 20, x=160, y=450)
			
			button('home', 'home', 5, 425, 50, 50, (0.2, 0.2, 0.2), (0.7, 0.7, 0.7), (0.5, 0.5, 0.5), (1, 1, 1))
			
			if self.button_down == 'home':
				self.app = 'home'
		
		# Creates a text button
		def button(title, name, x, y, w, h, bgcolor, txtcolor, altbgcolor, alttxtcolor):
			
			# Tests for click
			if self.pendingTouch.location in Rect(x, y, w, h):
				
				# Draws secondary colors
				draw_rect(x, y, w, h, (altbgcolor[0], altbgcolor[1], altbgcolor[2]))
				tint(alttxtcolor[0], alttxtcolor[1], alttxtcolor[2])
				
			else: # If not clicked
				
				# Draws primary colors
				draw_rect(x, y, w, h, (bgcolor[0], bgcolor[1], bgcolor[2]))
				tint(txtcolor[0], txtcolor[1], txtcolor[2])
				
				# Clears button var
				self.button_down = ''
				
			if self.Touch.location in Rect(x, y, w, h):
				
				# Sets variable to current button
				self.button_down = name
				
			# Draws text
			text(title, 'AvenirNext-Regular', 14, x + (w / 2), y + (h / 2))
		
		# Draws rectangle
		def draw_rect(x, y, w, h, color, outlinecolor=(0, 0, 0), outlinew=0):
			
			# Sets color and width of border
			stroke(outlinecolor[0], outlinecolor[1], outlinecolor[2])
			stroke_weight(outlinew)
			
			# Sets color of rect
			fill(color[0], color[1], color[2])
			
			# Draws rect
			rect(x, y, w, h)
		
		# Draws circle
		def draw_circ(x, y, r, color, outlinecolor=(0, 0, 0), outlinew=0):
			
			# Sets color
			fill(color[0], color[1], color[2])
			
			# Sets width and color of border
			stroke(outlinecolor[0], outlinecolor[1], outlinecolor[2])
			stroke_weight(outlinew)
			
			# Draws circle
			ellipse(x, y, r, r)

		# Draws line
		def draw_line(x, y, x2, y2, thickness, color):
			
			# Sets color and width
			stroke(color[0], color[1], color[2])
			stroke_weight(thickness)
			
			# Draws line
			line(x, y, x2, y2)
		
		# Draws textbox
		def txtbx(x, y, w, h, font, bgcolor, txtcolor):
			pass
		
		# Draws checkbox
		def checkbx(x, y, name):
			
			# Tests for click
			if self.pendingTouch.location in Rect(x, y, 20, 20):
				
				# Draws secondary color
				draw_rect(x, y, 20, 20, (0.6, 0.6, 0.6))
				
			if self.Touch.location in Rect(x, y, 20, 20):
				
				# If selected and not already clicked
				if name in self.chckbx_true and self.repeat == 1:
					
					# Removes name from selected
					self.chckbx_true.remove(name)
					
				# Else if not selected and not already clicked
				elif self.repeat == 1:
					
					# Adds name to selected
					self.chckbx_true.append(name)
				
				# Stops repeats
				self.repeat = 0
				
			else: # If not clicked
			
				# Draws primary color
				draw_rect(x, y, 20, 20, (0.8, 0.8, 0.8))
				
				# Resets repeat
				self.repeat = 1
				
			# Tests if selected
			if name in self.chckbx_true:
				
				# Draws check
				draw_line(x + 18, y + 18, x + 9, y + 2, 2, (0, 0, 1))
				draw_line(x + 10, y + 2, x + 2, y + 10, 2, (0, 0, 1))
		
		# Creates a popup
		def popup(title, message, name, btn1='Okay', btn2='Cancel'):
			
			# Tests for current popup
			if self.popup == name:
				
				# Draws main rect
				draw_rect(60, 85, 200, 250, (1, 1, 1), outlinew=1)
				
				# Draws text
				tint(0, 0, 0)
				text(title, 'AvenirNext-Regular', 20, 160, 315)
				text(message, 'AvenirNext-UltraLight', 14, 160, 210)
				
				# Tests if button 1 is used
				if btn1 != '':
					
					# Draws button 1
					button(btn1, 'btn1popup', 65, 125, 190, 30, (1, 1, 1), (0, 0, 0), (0, 0, 0), (1, 1, 1))
					
				# Draws button 2
				button(btn2, 'btn2popup', 65, 90, 190, 30, (1, 1, 1), (0, 0, 0), (0, 0, 0), (1, 1, 1))
		
		# Draws a button used to open an app
		def applink(app, color, bgcolor, mode=0):
			
			# Calculates x and y
			x = (self.apps_drawn + 4) % 4 * 76 + 16
			y = 500 - (105 * (floor(self.apps_drawn / 4) + 1))
			
			if mode == 0:
				# Draws rect for button
				draw_rect(x, y, 60, 60, (bgcolor[0], bgcolor[1], bgcolor[2]))
			
			elif mode == 1: # Group of apps
			
				draw_rect(x, y, 60, 60, (0.8, 0.8, 0.8))
				
				# Draws nine rects
				xList = [x + 2.25, x + 21.5, x + 40.75]
				yList = [y + 2.25, y + 21.5, y + 40.75]
				for valx in xList:
					for valy in yList:
						draw_rect(valx, valy, 17, 17, (bgcolor[0], bgcolor[1], bgcolor[2]))
			
			# Draws shadow
			if bgcolor == (0, 0, 0):
				tint(0.2, 0.2, 0.2)
			else:
				tint(bgcolor[0] - 0.2, bgcolor[1] - 0.2, bgcolor[2] - 0.2)
			text(app[0].lower(), 'AvenirNext-Regular', 44, x + 33, y + 27)
			
			# Draws letter on button
			tint(color[0], color[1], color[2])
			text(app[0].lower(), 'AvenirNext-Regular', 44, x + 30, y + 30)
			
			# Draws name of app under button
			tint(0, 0, 0)
			text(app, 'AvenirNext-UltraLight', 14, x + 30, y - 10)
			
			# If hovered over
			if self.pendingTouch.location in Rect(x, y, 60, 60):
				
				# Darken icon
				fill(0.5, 0.5, 0.5, 0.5)
				rect(x, y, 60, 60)
			
			# If clicked on
			if self.Touch.location in Rect(x, y, 60, 60):
				
				# Set app
				self.app = app
			
			# Check to stop drawing apps
			self.apps_drawn += 1
			if self.apps_drawn >= self.num_apps:
				self.apps_drawn = 0
			
		def lockscrn(mode=0):
			pass
			
		def run_app(app):
			
			if app == 'test':

				new_bg(app)
				draw_rect(200, 200, 50, 50, (0, 0, 1), (0, 0, 0), 2)
				tint(0, 0, 0)
				text('Hi', 'AvenirNext-UltraLight', 20, x=100, y=100)
				draw_circ(150, 300, 70, (1, 1, 0))
				draw_line(0, 0, 50, 50, 2, (0.5, 1, 0.5))
				button('click me', 'test', 20, 200, 100, 30, (0, 0, 0), (1, 1, 1), (0.5, 0.5, 0.5), (0.3, 0.3, 0.3))
				if self.button_down == 'test':
					if 'toggle' in self.chckbx_true:
						self.popup = 'On'
					else:
						self.popup = 'Off'
						
				if self.popup == 'On':
					popup('Checkbox', 'The checkbox is selected', 'On', 'Deselect', 'Close')
				elif self.popup == 'Off':
					popup('Checkbox', 'The checkbox isn\'t selected', 'Off', 'Select', 'Close')
				
				if self.button_down == 'btn2popup':
					self.popup = ''
				elif self.button_down == 'btn1popup':
					if 'toggle' in self.chckbx_true:
						self.chckbx_true.remove('toggle')
					else:
						self.chckbx_true.append('toggle')
				
				checkbx(100, 50, 'toggle')
				
			if app == 'App Store':
				new_bg(app)
				
			if app == 'Settings':
				new_bg(app)
				
			if app == 'Music':
				new_bg(app)
			
			if app == '4explore':
				new_bg(app)
			
			if app == 'home':
				
				background(1, 1, 1)
				
				draw_rect(0, 0, 320, 80, (0, 0, 0))
				
				tint(1, 1, 1)
				time = curr_time()[0] + ':' + curr_time()[1] + ':' + curr_time()[2] + ' ' + curr_time()[3]
				text(time, 'AvenirNext-UltraLight', 44, 160, 40)
				
				applink('test', (1, 1, 1), (0, 0, 1))
				applink('App Store', (1, 1, 1), (1, 0, 0))
				applink('Settings', (1, 1, 1), (0.6, 0.6, 0.6))
				applink('Music', (1, 1, 1), (0.50, 0.00, 0.50))
				applink('4explore', (1, 1, 1), (0, 0, 0))
				
		run_app(self.app)
		
		if self.Touch != Touch(-100, -100, -100, -100, 0):
			self.Touch = Touch(-100, -100, -100, -100, 0)
		
	def touch_began(self, touch):
		self.pendingTouch = touch
		
	def touch_moved(self, touch):
		self.pendingTouch = touch
		
	def touch_ended(self, touch):
		if self.pendingTouch == touch:
			self.Touch = touch
			self.pendingTouch = Touch(-100, -100, -100, -100, 0)

run(os(), PORTRAIT)
