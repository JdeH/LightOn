cities = list (('Londen', 'Paris', 'New York', 'Berlin')) # Construct list object from 'tuple' of 4 string objects
print ('Class is:', type (cities))                        # Verify that it is indeed a list

print ('Before sorting:', cities)                         # Print the unsorted list
cities.sort ()                                            # Sort the list
print ('After sorting: ', cities)                         # Print the sorted list