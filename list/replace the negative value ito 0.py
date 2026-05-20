lst = [3, -1, 5, -7, 2, -4]
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print("Updated list:", lst)