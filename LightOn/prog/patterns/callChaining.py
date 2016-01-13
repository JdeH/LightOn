import itertools

class Accessor:
	def __init__ (self, table):
		self.table = table

	def __getattr__ (self, name):
		return self.row [self.table.fieldDict [name]]
		
	def __call__ (self, row):
		self.row = row
		return self
		
def FROM (*tables):
	if len (tables) == 1:
		return tables [0]
	else:
		result = TABLE (*itertools.chain (*(table.fieldNames for table in tables)))
		result.rows = set (
			tuple (itertools.chain (*row))
			for row in itertools.product (*(table.rows for table in tables))
		)
		return result
		
class Descending:	
	def __ror__ (self, first):
		self.field = first
		return self
		
DESC = Descending ()
	
def tuplize (any):
	return any if type (any) == tuple else (any,)
	
class TABLE:
	def __init__ (self, *fieldNames):
		self.fieldNames = fieldNames
		self.fieldDict = {fieldName: index for index, fieldName in enumerate (self.fieldNames)}
		self.accessor = Accessor (self)
		self.rows = set ()

	def __call__ (self, **aliases):
		result = TABLE (*(
			(aliases [fieldName] if fieldName in aliases else fieldName)
			for fieldName in self.fieldNames
		))
		result.rows = self.rows # Only copy reference, since nothing is changed
		return result
		
	def __contains__ (self, fieldOrTuple):
		return tuplize (fieldOrTuple) in self.rows
		
	def INSERT (self, *rows):
		self.rows = set (rows)
		
	def WHERE (self, function):
		result = TABLE (*self.fieldNames)
		result.rows = {row for row in self.rows if function (self.accessor (row))}
		return result
		
	def SELECT (self, function):
		result = TABLE (*tuplize (function (self.accessor (self.fieldNames))))
		result.rows = {tuplize (function (self.accessor (row))) for row in self.rows}
		return result
		
	def ORDER_BY (self, function):
		aList = list (self.rows)
		
		def sortParamPair (descendingOrField, index):
			isDescending = isinstance (descendingOrField, Descending)
			keyGetter = (
				lambda row: tuplize (function (self.accessor (row))) [index] .field
			) if isDescending else (
				lambda row: tuplize (function (self.accessor (row))) [index]
			)
			return (keyGetter, isDescending)
	
		sortParamPairs = [
			sortParamPair (descendingOrField, index)
			for index, descendingOrField in enumerate (
				tuplize (function (self.accessor (self.fieldNames)))
			)
		]
		
		aList = list (self.rows)
		for keyGetter, isDescending in reversed (sortParamPairs):
			aList.sort (key = keyGetter, reverse = isDescending)
					
		return Cursor (self, aList)
		
class Cursor:
	def __init__ (self, table, aList):
		self.table = table
		self.aList = aList
		self.columnWidth = 15
		self.fieldFormatString = '{{:{}}}'.format (self.columnWidth)
		
	def __str__ (self):
		return '\n'.join (
			[	' '.join (
					[self.fieldFormatString.format (fieldName) for fieldName in self.table.fieldNames]
				),
				' '.join ([self.columnWidth * '_'] * len (self.table.fieldNames))
			] +
			[	' '.join (self.fieldFormatString.format (field) for field in row)
				for row in self.aList
			]			
		)
		
animals = TABLE ('species', 'gender', 'age', 'name', 'length')

animals.INSERT (
	('horse', 'male', 15, 'henry', 1.8),
	('human', 'female', 22, 'wilma', 1.7),
	('human', 'male', 30, 'john', 1.5),
	('human', 'female', 20, 'mary', 1.9),
	('human', 'male', 26, 'robin', 1.7),
	('human', 'unknown', 25, 'robin', 1.8),
	('human', 'female', 27, 'robin', 1.4),
	('ape', 'female', 5, 'benji', 1.1)
)

eats = TABLE ('animalSpecies', 'plantSpecies')

eats.INSERT (
	('horse', 'gras'),
	('horse', 'oats'),
	('human', 'oats'),
	('human', 'lettuce'),
	('human', 'banana'),
	('ape', 'banana')
)

plants = TABLE ('species', 'length')

plants.INSERT (
	('gras', 0.3),
	('oats', 0.5),
	('banana', 0.2)
)

primateFood = TABLE ('species', 'kind')

primateFood.INSERT (
	('oats', 'wild'),
	('banana', 'wild'),
	('banana', 'cultivated')
)

adultsCursor = (
	FROM (animals) .
	WHERE (lambda r: r.species == 'human' and r.age > 10) .
	SELECT (lambda r: (r.gender, r.name, r.age)) .
	ORDER_BY (lambda r: (r.name, r.age | DESC))
)

print ('\n', adultsCursor)

menu = (
	FROM (
		animals (species = 'aSpecies', length = 'animalLength'),
		eats,
		plants (species = 'pSpecies', length = 'plantLength')
	) .
	WHERE (lambda r: r.aSpecies == r.animalSpecies and r.plantSpecies == r.pSpecies) .
	SELECT (lambda r: (r.name, r.animalSpecies, r.animalLength, r.plantSpecies, r.plantLength))
)
	
menuCursor = \
	FROM (menu). \
	ORDER_BY (lambda r: r.name)
	
print ('\n', menuCursor)

primateCursor = (
	FROM (menu) .
	WHERE (lambda r: (r.plantSpecies, 'cultivated') in (
		FROM (primateFood) .
		SELECT (lambda r: (r.species, r.kind))
	)) .
	ORDER_BY (lambda r: r.name)
)

print ('\n', primateCursor)
