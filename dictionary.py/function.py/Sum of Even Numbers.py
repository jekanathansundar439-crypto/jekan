# Sum of Even Numbers
numbers = [1, 2, 3, 4, 5, 6]
even_num = list(filter(lambda x: x % 2 == 0, numbers))
result = sum(even_num)
print(result)