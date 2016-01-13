even_numbers = []
for index in range (10):
    even_numbers.append (2 * (index + 1))
print ('Even numbers:', even_numbers)
    
squared_numbers = []
for even_number in even_numbers:
    squared_numbers.append (even_number * even_number)
print ('Squared numbers:', squared_numbers)