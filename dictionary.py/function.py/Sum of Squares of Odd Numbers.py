# Sum of Squares of Odd Numbers
numbers = [1, 2, 3, 4, 5]
result1 = list(filter(lambda x: x % 2 != 0, numbers))
result2 = list(map(lambda x: x ** 2, result1))
result = sum(result2)
print(result)