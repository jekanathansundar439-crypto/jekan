nums = [10, 25, 5, 40, 15]

largest = nums[0]

for n in nums:
    if n > largest:
        largest = n

print("Largest number:", largest)