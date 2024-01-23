# alters how a function works
# defined with @ symbol

def logtime(func):
    def wrapper():
        val = func
        return val
    return wrapper

@logtime
def hello():
    print("hi")


hello()