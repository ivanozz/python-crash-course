for value in range(1, 5):
	print(value)

# or
numbers = list(range(1,5))
print(numbers)

# список четных чисел
numbers = list(range(2, 11, 2))

squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

max(squares)
min(squares)
sum(squares)

#or 

squares = [value**2 for value in range(1,11)]
print(squares)
