import itertools
# Module itertools is part of the Python standard library and contains tools for iterators
# An iterator resembles a list, but different from a list, an iterator does not hold all of its elements
# It produces them on the fly, without storing them all at the same time in memory
# Because this sounds a bit alien, just try to follow how iterators are used here

class Accessor:
# Our 'database' will consist of tables, each TABLE holding a unordered set of rows
# While these rows are just tuples whose components can be addressed by indices,
# they an also be addressed by field name, using a part of the TABLE called the field dictionary
# The task of an Accessor is to make this addressing by name instead of by index possible
# The Accessor class does this by introducing a kind of virtual attributes, one for each field name

	def __init__ (self, table):
	# Each Table will create an Accessor for itself and pass itself as parameter to its constructor
	
		self.table = table
		# At this point the Accessor knowns to which TABLE it belongs

	def __getattr__ (self, name):
	# Methods between starting and ending with __ are special
	# In Python accessing anObject.anAttribute results in calling anObject.__getattr__ ('anAttribute')
	# By overriding (redefining) __getattr__ we make anObject.anAttribute lookup anAttribute in a special way
	
		return self.row [self.table.fieldDict [name]]
		# The expression self.table.fieldDict [aName] looks up the field index into the field dictionary
		# This index is then used to access the field as self.row [aFieldIndex]
		# But it looks like Accessor has no row attribute...
		
	def __call__ (self, row):
	# Overriding the __call__ special method means that objects of that class can be called as if they were functions
	# The call anAccessor (aRow) results in the call anAccessor.__call__ (aRow)
	
		self.row = row
		# This call results in creating a row attribute on the fly
		
		return self
		# After having created a row, anAccessor returns itself
		# Since it has a __getattr__, the call anAccessor (row) .aName results in
		# 1. Creating the right row attribute
		# 2. Accessing the field with name aName from that row using __getattr__
		
def FROM (*tables):
# The *tables means that this function will put all its parameters into a list called tables

	if len (tables) == 1:
	# The list of tables has length one, only one table is passed in
	
		return tables [0]
		# Return that one table 
		
	else:
	# The list contains more than one TABLE
	
		result = TABLE (*itertools.chain (*(table.fieldNames for table in tables)))
		# Merge all the lists of fieldNames of these tables into
		# one long list of fieldNames for the resulting TABLE
		
		result.rows = set (tuple (
		# Step 3. Convert the resulting list of rows into an unordered set,
		#         assign it to the row set of the result TABLE
		
			itertools.chain (*row)) for row in
			# Step 2. For each row of the carthesian product, merge its subrows
			
			itertools.product (*(table.rows for table in tables)
			# Step 1. Compute the carthesian product,
			#         holding all combinations of subrows from the individual tables
		))
		return result
		# Return the new, merged TABLE, which is the join of the individual tables (Google for 'SQL full join')
		
class Descending:
# Objects of this class are used as an indicator that sort order in the ORDER_BY method has to be descending
	def __ror__ (self, first):
	# 'reverse or', this gives the | operator a new meaning
	# If DESC is of class Descending, then DESC.__ror__ (firstObject) can also be written as: firstObject | DESC
	# If it had been __or__ rather than __ror__, then DESC.__or__ (lastObject) could
	# have been written as: DESC | lastObject
	
		self.field = first
		# In the process of evaluating expression firstObject | DESC, DESC.field gets value firstObject
		
		return self
		# So expression firstObject | DESC will return the object DESC, having an attribute firstObject
		
DESC = Descending ()
	
def tuplize (any):
	return any if type (any) == tuple else (any,)
	# If any is already a tuple, that tuple will be returned
	# If any is not already a tuple, the tuple (any,), having only one component, will be returned
	# So a single value will automatically be converted to  tuple with that value as only component
	
class TABLE:
# Our 'database' consists of tables

	def __init__ (self, *fieldNames):
	# *fieldNames means that the parameters of the constructor call will be placed in to a list
		self.fieldNames = fieldNames
		# This list of fieldNames is stored in the TABLE object
		
		self.fieldDict = {fieldName: index for index, fieldName in enumerate (self.fieldNames)}
		# The field dictionary makes it possible to look up the field index by name
		# So expression self.fieldDict ('aFieldName') gives the index of field 'aFieldName' in each row tuple
		
		self.accessor = Accessor (self)
		# The accessor object can be coupled to a row by the expression self.accessor (aRow)
		# self.accessor.aFieldName then returns the right field of that row as explained with the Accessor class
		
		self.rows = set ()
		# The rows of a TABLE are unordered, so they are represented by a Python set, not by a list

	def __call__ (self, **aliases):
	# This function makes it possible to rename the fields of a 'database' TABLE
	#
	# aTable (someParameters) is equivalent to aTable.__call__ (someParamters)
	#
	# The call aTable (fieldName1 = 'newFieldName1', fieldName2 = 'newFieldName2') uses named parameters
	# Named parameters are allowed with any function or method call in Python
	# In this case it will result in  aTable.__call__ (fieldName1 = 'newFieldName1', fieldName2 = 'newFieldName2')
	#
	# The **aliases notation means that the values of the named parameters will be stored into the aliases dictionary
	# The names of the parameters will be the keys to their values in that Python dict
	# So e.g. aliases ['fieldName1'] will return 'newFieldName1'
		
		result = TABLE (*(
			(aliases [fieldName] if fieldName in aliases else fieldName)
			for fieldName in self.fieldNames
		))
		# The resulting table will have the aliases as field names instead of the original ones
		
		result.rows = self.rows
		# The contents of the new table does not change, 
		
		return result
		# Return that new table, according to the Call Chaining pattern
		
	def __contains__ (self, fieldOrTuple):
		return tuplize (fieldOrTuple) in self.rows
		# Looks up a certain tuple of field values
		# If it's a single value, tuplize will make it a tuple of 1 component
		
	def INSERT (self, *rows):
	# *rows will turn the parameters of a call to INSERT into a list called rows
		self.rows = set (rows)
		# This list of rows is converted to a set and assigned to the row attribute of TABLE
		
	def WHERE (self, function):
		result = TABLE (*self.fieldNames)
		# An empty result TABLE with the same field names as TABLE self is created

		result.rows = {row for row in self.rows if function (self.accessor (row))}
		# Only rows for which function returns True will be inserted into the result TABLE
		
		return result
		# The result TABLE is returned, once again allowing Call Chaining
		
	def SELECT (self, function):
		result = TABLE (*tuplize (function (self.accessor (self.fieldNames))))
		# The field names are treated as just another row
		# The accessor turns them in to an object with attributes as explained with the Accessor class
		# The attributes in this case will contain their own names,
		# since this 'row' contains the field names as fields
		# Calling function (accessor (self.fieldNames)) will return a selected field names
		
		result.rows = {tuplize (function (self.accessor (row))) for row in self.rows}
		# Calling function (accessor (row)) will return the selected
		# field values matching the selected field names
		# In this set comprehension, this selection of field values is done for all rows
		# A set comprehension is like a list comprehension, but it produces a set instead of a list
		
		return result
		# Return the resulting TABLE, according to the Call Chaining pattern
		# It fill contain only the selected field names and the matching selected fields
		
	def ORDER_BY (self, function):
	# The function passed to ORDER_BY can e.g. be lambda r: (r.name, r.age | DESC)
	# This means: first sort ascending on name, and after that descending on age
		aList = list (self.rows)
		# Turn the set of rows into a list, since sets cannot be ordered at all
		
		def sortParamPair (descendingOrField, index):
		# Parameter descendingOrField will e.g. be r.name, or r.age | DESC
		# If it's indeed r.age | DESC, it will evaluate to the DESC object, and DESC.field have value age
		# Look at the explanation of class Descending to understand this
		#
		# Parameter index will hold the field index matching the descendingOrField parameer
			isDescending = isinstance (descendingOrField, Descending)
			# If descendingOrField evaluates to a DESC object,
			# sorting on field DESC.field should be done descending
			
			keyGetter = (
			# keyGetter should be assigned a function that returns the value of the field to sort on
			
				lambda row:
				# This lambda is used for a descending sort, it has to unpack the field from DESC
					tuplize (function (
						self.accessor (row)
						# The attributes of the accessor objects are
						# now the field values of this row
						# Some may be wrapped in DESC
					))
					# At this point we have the a tuple of field values to sort on,
					# some wrapped in DESC
					
					[index]
					# At this point we have the right field from that tuple, as indicated by index
					# but the sort is descending, so it will be wrapped in DESC
					
					.field
					# We unwrap it by returning DESC.field
				
				) if isDescending else (
				# Use the lambda function above in case a DESC indicator is present,
				# else use the one below
				
				lambda row:
				# This lambda is used for an ascending sort, it doesn't have to unpack the field
					tuplize (function (
						self.accessor (row)
						# The attributes of the accessor object are now the
						# field values of this row
					))
					# At this point we have the a tuple of field values to sort on
					
					[index]
					# At this point we have the right field from that tuple, as indicated by index
			)
			
			return (keyGetter, isDescending)
			# We return the lambda function that returns the right field,
			# and wether or not the sort on that field is descending
			# This tuple is called the sort parameter pair
			
		sortParamPairs = [
			sortParamPair (descendingOrField, index)
			for index, descendingOrField in enumerate (
				tuplize (function (
					self.accessor (self.fieldNames)
					# The attributes of the accessor object are now the field names,
					# some of them wrapped in DESC
				))
				# At this point we have a tuple of field names, some wrapped in DESC
			)
			# We now pair each field name, some wrapped in DESC, with its index
		]
		
		aList = list (self.rows)
		for keyGetter, isDescending in reversed (sortParamPairs):
		# Going through the keys in the right order
			aList.sort (key = keyGetter, reverse = isDescending)
			# Sort the list on that keys successively
					
		return Cursor (self, aList)
		# Return a Cursor for that list
		# A Cursor is a ordered list of rows
		# It has a multiline string representation featuring a header line and then a line for each row
		
class Cursor:
	def __init__ (self, table, aList):
		self.table = table
		self.aList = aList
		self.columnWidth = 15
		self.fieldFormatString = '{{:{}}}'.format (self.columnWidth)
		
	def __str__ (self):
		# The __str__ special function of a class lays down how objects of this
		# class are converted to strings.
		# Such conversion e.g. takes place of the object is printed
		
		return '\n'.join (
			# Glue the header and the rows together with linefeeds in between,
			# so each will be on its own line
			[	' '.join (
					[self.fieldFormatString.format (fieldName) for fieldName in self.table.fieldNames]
				),
				# Header line containing field names, glued together with blanks
				
				' '.join ([self.columnWidth * '_'] * len (self.table.fieldNames))
				# Line of underscores under each field name to separate them from the rows,
				# glued together with blanks
			] +
			[	' '.join (self.fieldFormatString.format (field) for field in row)				
				for row in self.aList
				# Many lines of field values glued together with blanks, one line for each row
			]			
		)
		
animals = TABLE ('species', 'gender', 'age', 'name', 'length')
# Create animals table, specifying field names

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
# Insert rows into the animals table

eats = TABLE ('animalSpecies', 'plantSpecies')
# Create table eats, specifying field names

eats.INSERT (
	('horse', 'gras'),
	('horse', 'oats'),
	('human', 'oats'),
	('human', 'lettuce'),
	('human', 'banana'),
	('ape', 'banana')
)
# Insert rows into eats table

plants = TABLE ('species', 'length')
# Create plants table, specifying field names

plants.INSERT (
	('gras', 0.3),
	('oats', 0.5),
	('banana', 0.2)
)
# Insert rows in to plants table

primateFood = TABLE ('species', 'kind')
# Create primateFood table

primateFood.INSERT (
	('oats', 'wild'),
	('banana', 'wild'),
	('banana', 'cultivated')
)
# Insert rows into primateFood table

adultsCursor = (
	FROM (animals) .
	WHERE (lambda r: r.species == 'human' and r.age > 10) .
	SELECT (lambda r: (r.gender, r.name, r.age)) .
	ORDER_BY (lambda r: (r.name, r.age | DESC))
)
# FROM, WHERE, SELECT and ORDER_BY are called one after another,
# according to the Call Chaining pattern

print ('\n', adultsCursor)
# The string representation of the resulting Cursor is printed

menu = (
	FROM (
		animals (species = 'aSpecies', length = 'animalLength'),
		eats,
		plants (species = 'pSpecies', length = 'plantLength')
	) .
	WHERE (lambda r: r.aSpecies == r.animalSpecies and r.plantSpecies == r.pSpecies) .
	SELECT (lambda r: (r.name, r.animalSpecies, r.animalLength, r.plantSpecies, r.plantLength))
)
# A full join (Google) is created, some field names of the
# animals and plants tables are replaced by aliases
# This prevents confusion with identical field names of the eats table
# The end product here is not a Cursor but a TABLE, since that is what SELECT returns
	
menuCursor = \
	FROM (menu). \
	ORDER_BY (lambda r: r.name)
# Now we have our Cursor
	
print ('\n', menuCursor)
# The string representation of the resulting Cursor is printed

primateCursor = (
	FROM (menu) .
	WHERE (lambda r: (r.plantSpecies, 'cultivated') in (
		FROM (primateFood) .
		SELECT (lambda r: (r.species, r.kind))
	)) .
	ORDER_BY (lambda r: r.name)
)
# This type of query is called a 'nested query'
# It uses information from the primateFood table to select rows from
# the menu table that was constructed earlier 

print ('\n', primateCursor)
# Print the result of the nested query

