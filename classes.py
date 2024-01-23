class dog:

    def bark(self):
        print("woof")

#roger = dog()
#print(type(roger)) # <class '__main__'.dog>
#roger.bark() # woof

class doge:

    # constuctor used to init properties 
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bork(self):
        print("woofz")

#sam = doge('Sam', '2') # since constructor is used, input values
#print(sam.name) # Sam
#print(sam.age) # 2
#sam.bork() # woofz


class mark:

    def __init__(self, student, marks):
        mark.student = student
        mark.marks = marks

peter = mark("Peter", 98)

#print(mark.student)
#print(mark.marks)

# inheritance
class animal:
    def walk(self): #remember to add self to point to current object instance
        print("on the way...")

class cat(animal):
    def __init__(self, name, type):
        self.name = name # inits
        self.type = type

    def roar(self): # functions
        print("MEOOOOW")

timbles = cat("Timbles", "Spicy")
print(timbles.name) # inits, thus no () and in print()
print(timbles.type)
timbles.walk() # funtions, thus no need for print
timbles.roar()