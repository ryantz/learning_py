# has key value pairs

dog = {"name":"Cooper", "age":"5"}

print(dog['name'])
print(dog['age'])

#changing values in a dict
dog['name'] = "Bradley"
print(dog['name'])

print(dog.get('name'))
print(dog.get('test','default'))

# retrieves key and removes the item
dog.pop('name')
print(dog)

dog.popitem()
print(dog)

dog = {"name":"Cooper", "age":"5"}

print('name' in dog) # True (checking if there is the kye 'name' in dog)

print(list(dog.keys())) #printing all the keys in the dict
print(list(dog.values())) # printing all values in the dict
print(list(dog.items())) # printing as key value tuples

# adding and removing dict elements
dog['fav food'] = "Chicken"
print(list(dog.items()))
del dog['age']
print(list(dog.items()))

# copying dictionary items
dogCopy = dog.copy()
print(dogCopy)