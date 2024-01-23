name = "Roger"
name += " is a dude"
number = 8

print(type(str(8))) # <class 'str'>
print(name + " is " +  str(number))
print(""" O
      
      
      Hi""") # multi line strings

#name = "Roger is a dude"
print(name.replace("dude","gal"))
print(len(name))

# in operator
print("retr" in "firetruck")

# escaping to add special characters \ helps to escape ""
print("hello i am \"the badedest man\"")

print(name[1]) # returns o 
print(name[-2]) # returns e (-1 is the last element in the str)
print(name[:]) # print all [start:stop before]
print(name[0:-2]) # "Roger is a du" index 0 to -2
print(name[:3]) # index 0 to 3
print(name[4:]) # starts from index 4





