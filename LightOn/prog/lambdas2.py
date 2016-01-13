def power (x, n):   # Define free function, outside any class, no self parameter
    result = x
    for i in range (n - 1):     # Note that i runs from 0 to n - 2
        result *= x             # so this is performed n - 1 times     
    return result
    
test = power (2, 8)             # Call free function, no object before the dot
print ('test:', test)
    
def apply (operation, numbers):   # Define free function that applies compute to numbers
    return [operation (number) for number in numbers] # Return list of computed numbers
    
sides = [1, 2, 3]

areas = apply (lambda side: power (side, 2), sides)   # Define area function and pass it to apply
volumes = apply (lambda side: power (side, 3), sides) # Define volume function and pass it to apply

print ('sides:', sides)
print ('areas:', areas)
print ('volumes:', volumes)