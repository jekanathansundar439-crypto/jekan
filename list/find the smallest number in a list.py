nums = [10, 25, 5, 40, 15]

smallest = nums[0]

for n in nums:
    if n < smallest:
        smallest = n

print("smallest number:", smallest)