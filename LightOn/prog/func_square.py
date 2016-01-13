even_numbers = [2 * (index + 1) for index in range (10)]       # Create [2, 4, ..., 20]
print ('Even numbers:', even_numbers)

squared_numbers = [number * number for number in even_numbers] # Compute list of squared numbers
print ('Squared numbers:', squared_numbers)