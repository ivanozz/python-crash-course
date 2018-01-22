user_0 = {
    'username': 'eric',
    'first': 'enric',
    'last': 'fermik'
}

# вывод словаря
for key, value in user_0.items() :
	print("\nKey: " + key);
	print("Value: " + value);

# вывод ключей
for key in user_0.keys() :
	print(name.title())

# упорядочивание ключей
for key in sorted(user_0.keys()) :
	print(name.title())

# вывод значений
for value in user_0.values() :
	print(value)

# вывод значений без дублей
for value in set(user_0.values()) :
	print(value)
	
# вложение списка в словарь
languages = {
	'jen': ['ruby', 'c'],
	'john': ['python', 'scala'],
}
