lst = [10, 20, 5, 40, 30]

largest = lst[0]
second = lst[0]

for i in lst:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second largest:", second)
















#  ITERATION
#👉 Start:
#largest = 10
#second = 10
#🔄 Iteration:
#🔹 1st iteration:
#i > largest? → 10 > 10 ❌
#i > second and i != largest? → ❌
#👉 No change
#largest = 10, second = 10
#🔹 2nd iteration:
#i = 20
#20 > 10 ✅
#👉 Update:
#second = 10
#largest = 20

#Now:

#largest = 20, second = 10
#🔹 3rd iteration:
#i = 5
#5 > 20 ❌
#5 > 10 ❌#
#👉 No chanage
#🔹 4th iteration:
#i = 40
#40 > 20 ✅
#👉 Update:
#second = 20
#largest = 40

#Now:

#largest = 40, second = 20
#🔹 5th iteration:
#i = 30
#30 > 40 ❌
#30 > 20 ✅ and not equal to largest
#👉 Update:
#second = 30