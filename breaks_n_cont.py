items = [1,2,3,4,5]

for item in items:
    if item == 2:
        continue # 1 3 4 5 (notice 2 is missing)
        #break # 1
    print(item)

