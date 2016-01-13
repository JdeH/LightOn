even_numbers = []
for index in range (10):
    even_numbers.append (2 * (index + 1))
print ('Even numbers:', even_numbers)
    
total = 0
for even_number in even_numbers:
    total += even_number
print ('Total:', total)
