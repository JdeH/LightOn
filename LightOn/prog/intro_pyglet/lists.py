import os
import random

import pyglet
from pyglet.gl import *

class View:
	orthoWidth = 1000
	orthoHeight = 750
	maxSpeed = 100		# / s
	
	def __init__ (self):
		self.window = pyglet.window.Window (				# Create resizable window
			640, 480, resizable = True, visible = False, caption = 'Lists'
		)
		
		self.window.on_resize = self.resize					# Will be called if window is resized
		self.window.on_draw = self.draw						# Will be called if window has to be redrawn
		
		self.window.set_location (							# Put window on middle of its screen
			(self.window.screen.width - self.window.width) // 2,
			(self.window.screen.height - self.window.height) // 2
		)
		
		self.window.clear ()								# Clear window
		self.window.set_visible (True)						# Show window once it's cleared

		self.sprites = []
		for fileName in os.listdir (						# For each file
			os.path.dirname (os.path.realpath(__file__))	# in the folder of this source file
		):	
			if fileName.endswith ('.png'):					# 	If its a .png file
				image = pyglet.image.load (fileName)		# 		Load it as an image
				image.anchor_x = image.width // 2			#		Lay its coordinate reference
				image.anchor_y = image.height // 2			#		in its middle
				self.sprites.append (						# 		Append to the sprite list
					pyglet.sprite.Sprite (image, 0, 0)		#		a sprite containing
				)

		pyglet.clock.schedule_interval (					# Install update callback that
			self.update, 1/20.								# will be called 60 times per s
		)
		pyglet.app.run ()									# Start pyglet engine

	def resize (self, width, height):						# When the user resizes the window
		glViewport (0, 0, width, height)					# Tell openGL window size
		
		glMatrixMode (GL_PROJECTION)						# Work with projection matrix
		glLoadIdentity ()									# Start with identity matrix
		glOrtho (											# Adapt it to orthographic projection
			-self.orthoWidth // 2, self.orthoWidth // 2,	# Lay origin in the middle
			-self.orthoHeight // 2, self.orthoHeight // 2,
			-1, 1
		)
		
		glMatrixMode (GL_MODELVIEW)							# Work with model matrix
		glLoadIdentity ()									# No transforms
		
	def update (self, deltaT):
		for sprite in self.sprites:							# For every sprite in the sprite lst
			sprite.x += random.uniform (-1, 1) * self.maxSpeed * deltaT	# Move it
			sprite.y += random.uniform (-1, 1) * self.maxSpeed * deltaT
		
	def draw (self):
		self.window.clear ()
		
		for sprite in self.sprites:							# For every sprite in the sprite list
			sprite.draw ()									# Draw it
			
View ()
 