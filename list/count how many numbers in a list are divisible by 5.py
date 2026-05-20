lst = [10, 12, 15, 22, 25, 30]

count = 0

for i in lst:
    if i % 5 == 0:
        count += 1

print("Count:", count)