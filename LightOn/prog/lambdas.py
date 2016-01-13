functions = [
    lambda x, y: x + y,    # Shorthand for anonymous add function
    lambda x, y: x * y     # Shorthand for anonymous multiply function
]


sum = functions [0] (3, 4) # Call the first lambda function

print ('3 + 4 =', sum)
print ('3 * 4 =', functions [1] (3, 4)) # Call the second lambda function