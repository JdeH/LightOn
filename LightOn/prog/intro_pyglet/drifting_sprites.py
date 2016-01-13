import os
import random

import pyglet
from pyglet.gl import *

class Sprite (pyglet.sprite.Sprite):
    def __init__ (self, fileName):
        image = pyglet.image.load (fileName)                # Load it as an image
        image.anchor_x = image.width // 2                   # Lay its coordinate reference
        image.anchor_y = image.height // 2                  # in its middle     
        pyglet.sprite.Sprite.__init__ (self, image, 0, 0)   # Initialize ancestor   

class Window (pyglet.window.Window):
    orthoWidth = 1000
    orthoHeight = 750
    maxSpeed = 100      # / s
    
    def __init__ (self):
        pyglet.window.Window.__init__ (                     # Initialize ancestor
            self, 640, 480, resizable = True, visible = False, caption = 'Drifting sprites'
        )
        
        self.on_resize = self.resize                        # Called if window is resized
        self.on_draw = self.draw                            # Called if window has to be redrawn
        
        self.set_location (                                 # Put window on middle of its screen
            (self.screen.width - self.width) // 2,
            (self.screen.height - self.height) // 2
        )
        
        self.clear ()                                       # Clear window
        self.set_visible (True)                             # Show window once it's cleared

        self.sprites = []
        for fileName in os.listdir (                        # For each file
            os.path.dirname (os.path.realpath(__file__))    # in the folder of this source file
        ):  
            if fileName.endswith ('.png'):                  #   If its a .png file
                self.sprites.append (Sprite (fileName))     #       Append to the sprite list

        pyglet.clock.schedule_interval (                    # Install update callback that
            self.update, 1/20.                              # will be called 60 times per s
        )
        pyglet.app.run ()                                   # Start pyglet engine

    def resize (self, width, height):                       # When the user resizes the window
        glViewport (0, 0, width, height)                    # Tell openGL window size
        
        glMatrixMode (GL_PROJECTION)                        # Work with projection matrix
        glLoadIdentity ()                                   # Start with identity matrix
        glOrtho (                                           # Adapt it to orthographic projection
            -self.orthoWidth // 2, self.orthoWidth // 2,    # Lay origin in the middle
            -self.orthoHeight // 2, self.orthoHeight // 2,
            -1, 1
        )
        
        glMatrixMode (GL_MODELVIEW)                         # Work with model matrix
        glLoadIdentity ()                                   # No transforms
        
    def update (self, deltaT):
        for sprite in self.sprites:                         # For every sprite in the sprite lst
            sprite.x += random.uniform (-1, 1) * self.maxSpeed * deltaT # Move it
            sprite.y += random.uniform (-1, 1) * self.maxSpeed * deltaT
        
    def draw (self):
        self.clear ()
        
        for sprite in self.sprites:                         # For every sprite in the sprite list
            sprite.draw ()                                  # Draw it
            
Window ()
 