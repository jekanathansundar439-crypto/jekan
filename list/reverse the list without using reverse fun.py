lst = [1, 2, 3, 4, 5]

rev = []
for i in lst:
    rev = [i] + rev

print("Reversed list:", rev)