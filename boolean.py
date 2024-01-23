# boolean is True or False

done = True

print(type(done)) # <class 'bool'>
print(isinstance(done, bool)) # True

# any() function returns True if any of the values are True
read1 = True
read2 = False

read_any = any((read1, read2)) #can be any iterable; list, tuple etc.
print(read_any) # True

# all() function returns True if all the values are true

read_all = all([read1, read2])
print(read_all) # False




