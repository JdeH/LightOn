import math

class Circle:
	def __init__ (self):
		self._setRadius (0)
		
	def _getRadius (self):
		return self._radius
	
	def _setRadius (self, value):
		self._radius = value
	
	def _getPerimeter (self):
		return 2 * math.pi * self._radius
	
	def _setPerimeter (self, value):
		self._radius = value / (2 * math.pi)
	
	def _getArea (self):
		return math.pi * self._radius * self._radius
	
	def _setArea (self, value):
		self._radius = math.sqrt (value / math.pi)

	radius = property (_getRadius, _setRadius)
	perimeter = property (_getPerimeter, _setPerimeter)
	area = property (_getArea, _setArea)
			
circle = Circle ()

circle.radius = 10
print ('radius = {}, perimeter = {}, area = {}'. format (circle.radius, circle.perimeter, circle.area))

circle.area = math.pi * 10000
print ('radius = {}, perimeter = {}, area = {}'. format (circle.radius, circle.perimeter, circle.area))
