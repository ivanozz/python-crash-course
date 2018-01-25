filename = 'pi_digits.txt'

# чтение файла целиком
with open(filename) as file_object:
	contents = file_object.read()
	print(contents)

# построчное чтение
with open(filename) as file_object: 
	for line in file_object:
		print(line)
		
# создание списка строк по содержимому файла
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line)
