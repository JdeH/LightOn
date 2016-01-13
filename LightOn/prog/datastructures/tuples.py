print ('\nA tuple is an ordered sequence of objects:')
planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
print (planets)
coordinates = (1, 2, 3)
print (coordinates)

print ('\nYou can pick out individual elements:')
ourPlanet = planets [2]
print (ourPlanet)

print ('\nIndices may be negative:')
lastPlanet = planets [-1]
print (lastPlanet)

print ('\nTo make tuples fast and compact, they are immutable, you can\'t change their components:')
try:
	planets [2] = 'Mother'
except Exception as e:
	print (e)
	
print ('\nYou can replace the tuple as a whole:')
coordinates = (4, 5, 6)
print (coordinates)
	
print ('\nYou can obtain a new tuple containing the sorted version of the old one:')
sortedPlanets = tuple (sorted (planets))
print (sortedPlanets)	

print ('\nTuples can be unpacked into function call parameters with *:')
print (sortedPlanets)
print (*sortedPlanets)
	
print ('\nTuples can be glued together, giving a new tuple:')
print (planets + coordinates)

print ('\nTuples can be polymorphic, containing different types of objects:')
class Test:
	pass
things = (0, 5.2, 'bike', (1, 2, 3), Test (), Test)
print (things)

print ('\nTo have a tuple of only one element, it must end with a comma:')
print (100,)

print ('\nThis comma at the end is also allowed for tuples of multiple elements:')
print (100, 200, 300,)

print ('\nYou can use tuple comprehensions like:')
even = tuple (i for i in range (20) if i % 2 == 0)	# Or: if not i % 2, since 0 means False
print (even)

