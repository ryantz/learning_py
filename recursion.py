# factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print("please enter the number you want to factorial:\n")
num = input() # input is a string
print(factorial(int(num))) # force it to be an int