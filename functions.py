def hello():
    print("Hello")

#hello()
    
def helloname(name, age):
    print("hello my name is " + name + " and I am "+ str(age))

#adding values to vars in func brackets are the default values
def hellodefault(name = "Ryan", age = 26):
    print("Hello i am " + name + " " + str(age))
    
#helloname("Ryan", 26)
#hellodefault()

# numbers are immutable in functions
def changeval(num):
    num = 5

val = 2
changeval(val)
#print(val) # 2

# return is a way to end a function
# returns a value. Not print
def trying(x):
    if x < 2:
        return x
    else:
        print("okok")

y = 1   
i = 2
#trying(y)
#print(trying(y)) #1
trying(i)


def hi(name):
    print("hello " + name + "!")
    return name, "2", "ok"

#hi("Ryan")
#print(hi("Ryan")) # ('Ryan', '2', 'ok')


