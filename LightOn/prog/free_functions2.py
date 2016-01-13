def power (x, n):   # Define free function, outside any class, no self parameter
    result = x
    for i in range (n - 1):     # Note that i runs from 0 to n - 2
        result *= x             # so this is performed n - 1 times     
    return result
    
test = power (2, 8)             # Call free function, no object before the dot
print ('test:', test)
    
def area (side):                # Define free function, computes area of square
    return power (side, 2)      # Call power function to do the job
    
def volume (side):              # Define free function, computes volume of cube
    return power (side, 3)      # Call power function to do the job
    
def apply (compute, numbers):   # Define free function that applies compute to numbers
    return [compute (number) for number in numbers] # Return list of computed numbers
    
sides = [1, 2, 3]               # List of side lengths
areas = apply (area, sides)     # Let apply compute areas by supplying area function
volumes = apply (volume, sides) # Let apply compute volumes by supplying volume function

print ('sides:', sides)
print ('areas:', areas)
print ('volumes:', volumes)