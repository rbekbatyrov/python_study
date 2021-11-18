#chapter4_bicycle2.py

bicycle = ['a', 'b', 'c', 'd']
for values in bicycle:
	print(values)
print('---')

bicycle = ['a', 'b', 'c', 'd']
for values in bicycle:
	print(f"{values.title()}, hey!")
	print(f"Hello, {values}")
print('---')

for values in range(1,5):
	print(values)
print('---')

numbers = list(range(1,5))
print(numbers)
print('---')

even_numbers = list(range(2,11,2))
print(even_numbers)
print('---')

squares = []
for values in range(1,11):
	squares.append(values**2)
print(squares)
print('---')

bicycle_1 = ['a', 'b', 'c']
bicycle_2 = bicycle_1[:]
print(bicycle_1)
print(bicycle_2)
