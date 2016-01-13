import math

class Circle:
	def __init__ (self):
		self.area = 0
		
	def _getRadius (self):
		return math.sqrt (self.area / math.pi)	# Use area property
	
	def _setRadius (self, value):
		self.area = math.pi * value * value 	# Use area property
	
	def _getPerimeter (self):
		return 2 * math.pi * self.radius		# Use radius property
	
	def _setPerimeter (self, value):
		self.radius = value / (2 * math.pi)		# Use radius property
	
	def _getArea (self):
		return self._area		# Only the area is actually stored!
	
	def _setArea (self, value):
		self._area = value

	radius = property (_getRadius, _setRadius)
	perimeter = property (_getPerimeter, _setPerimeter)
	area = property (_getArea, _setArea)
	
# Code below, using Circle, does not depend on what is actually stored, _radius or _area
	
circle = Circle ()

circle.radius = 10
print ('radius = {}, perimeter = {}, area = {}'. format (circle.radius, circle.perimeter, circle.area))

circle.area = math.pi * 10000
print ('radius = {}, perimeter = {}, area = {}'. format (circle.radius, circle.perimeter, circle.area))

print ('Attributes:', vars (circle))	# Print all 'real' attributes, so not the properties
