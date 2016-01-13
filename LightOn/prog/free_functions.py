def add (x, y):  # Free function, defined outside any class, no self parameter
    return x + y # It may return a result, but a method could do that also

def multiply (x, y):
    return x * y
    
sum = add (3, 4)  # Call the first free function

print ('3 + 4 =', sum)
print ('3 * 4 =', multiply (3, 4)) # Call the second free function