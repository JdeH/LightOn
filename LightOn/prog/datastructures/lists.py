print ('\nBelow you\'ll find the main things you can do with lists in Python')
print ('Some more possibilities in the Python documentation')

print ('\nLists are mutable ordered sequences of objects:')
stars = ['Regulus', 'Capella', 'Wega']
print (stars, '    Length =', len (stars))

print ('\nYou can concatenate lists with +')
stars2 = ['Aldebaran', 'Alamak'] + ['Mirach', 'Sirrah']
print (stars2)

print ('\nYou can concatenate lists also with +=')
stars += stars2
print (stars)

print ('\nYou can append elements:')
stars.append ('Betelgeuze')
print (stars)

print ('\nYou can change individual elements:')
stars [2] = 'Sirius'
print (stars)

print ('\nYou can lookup the index of elements:')
index = stars.index ('Sirius')
print ('Sirius found at index:', index)

print ('\nYou can take a slice of a list:')
threeStars = stars [1:4]
print (threeStars) 

print ('\nYou can replace a slice of a list:')
stars [1:4] = ['Sun', 'Polaris']
print (stars) 

print ('\nYou can also delete a slice of a list:')
stars [1:3] = []
print (stars)

print ('\nFor convenience there\'s a pop method. It can have parameters')
star = stars.pop ()
print (stars, '    Popped:', star)

print ('\nNegative indices are OK, also with slicing:')
starsMinusTwo = stars [1:-1]
print (starsMinusTwo)

print ('\nYou can obtain a new list containing the sorted version of the old one:')
sortedStars = sorted (stars, reverse = True)
print (sortedStars)

print ('\nBut you can also sort a list in place, since it\'s mutable:')
sortedStars.sort ()
print (sortedStars)

print ('\nList comprehensions are concise:')
starsWithI = [star for star in sortedStars if 'i' in star.lower ()]
print (starsWithI)

print ('\nThe for\'s can be nested:')
subscripts =  [(rowIndex + 1, columnIndex + 1) for rowIndex in range (3) for columnIndex in range (4)]
print (subscripts)

print ('\nCompare this one carefully to the previous one. What exactly are the differences and why?')
subscripts2 =  [[(rowIndex + 1, columnIndex + 1) for rowIndex in range (3)] for columnIndex in range (4)]
print (subscripts2)

print ('\nLists can be unpacked into function call parameters with *:')
print (sortedStars)
print (*sortedStars)

print ('\nLists can be zipped into eachother:')
l0 = [3 * i for i in range (5)]
l1 = [e + 1 for e in l0]
l2 = [e + 2 for e in l0]
lZipped = list (zip (l0, l1, l2))
print (lZipped)

print ('\nRepeated zips with parameter unpacking get back the original zipped list:')
print (list (zip (*lZipped)))
print (list (zip (*zip (*lZipped))))
