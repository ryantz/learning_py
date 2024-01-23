def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count # function ends
    
    return increment # still able to access count after function ends

increment = counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3