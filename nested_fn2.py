def count():
    count = 0 # local variable to count() function

    def increment():
        nonlocal count # using a variable outside of the function
        count += 1
        print(count)

    increment()

count()