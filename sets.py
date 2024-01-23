# sets are like tuples but not ordered or immutable
# like dictionaries with no keys

set1 = {"Roger", "Syd"}
set2 = {"Roger"}

# using mathematic sets
intersect = set1 & set2 # what is common
print(intersect) # Roger

union = set1 | set2
print(union)

difference = set1 - set2
print(difference) # Syd

# list of sets
print(list(set1))

# checking if something is in sets
print("Roger" in set1) # True