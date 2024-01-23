# a list can hold manyt types of data in one list
names = ["Ryan", "Brandon", "Sam", "Christian"]
jumble = ["Monday", 1, False]
empty_list = []

print(names.index("Ryan")) # 0
print(names[0]) # Ryan
print(names[:]) # print all [start:stop before]
print(names[-2]) # 2 from the last index (-1)
print(names[1:]) #print from index 1
print(names[:3]) #print until index 2
print(len(names)) # 4

# adding to a list
names.append("Sally") # only can add 1 element at a time
print(names)

names.extend(["Gorge", "Candy"])
print(names)

names += ["Mandy", "Alex"]
print(names)

# removing items
names.remove("Alex")
print(names)

# adding items at a certain point in a list
names.insert(3, "null") # adds at index 3 but does not remove previous
print(names)

names[3:3] = ["Gan", "Inda"] # adding multiple at index 3
print(names)

# sort a list with .sort()

#copy list
copylist = names[:]
print(copylist)

