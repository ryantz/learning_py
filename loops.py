# a while loop will continue executing until it is False
# it is important to include a statement to push False
count = 0

while count < 10:
    print("The count is " + str(count))
    count += 1

print("The loop has ended")

# for loops
items = [1,2,3,4]

for a in items:
    print(a)

for i in range(4): # starts from 0 and contains 4 times 
    print(i) # 0 1 2 3


for index, item in enumerate(items): # enumerate gets the index
    print(index, item)

    
