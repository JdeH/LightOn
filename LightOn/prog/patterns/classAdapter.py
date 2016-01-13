class MovementPlanner:
	def __init__ (self, routeSegmenter):
		self.routeSegmenter = routeSegmenter

	def batch (self, *locationPairs):	# * means convert parameters to list
		print ()
		print ('Starting moves')
		print ()
		for locationPair in locationPairs:
			self.routeSegmenter.move (locationPair)
		print ('Moves ready')
	
class RouteSegmenter:
	def move (self, locationPair):
		raise Exception ('Abstract method called: RouteSegmenter.move')
		
class AscSequenceControl:
	def get (self, location):
		print ('Picked up container at location:', location)
		
	def put (self, location):
		print ('Put down container at location:', location)
	
class AscRouteSegmenter (RouteSegmenter, AscSequenceControl):
	def move (self, locationPair):
		self.get (locationPair [0])
		self.put (locationPair [1])
		print ()
		
MovementPlanner (AscRouteSegmenter ()) .batch (
	('3A3', '2K1'),
	('3A2', '2K2'),
	('2C1', '9M3'),
	('9R4', '1A1'),
	('9R3', '1A2')
)
