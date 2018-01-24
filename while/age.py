age = int(input('How old are you? '))

if age >= 18 :
	print(True)
else :
	print(False)
	
current_number = 1

while current_number <= 5 :
	print(current_number)
	current_number += 1
	
prompt = 'tell me something: '
prompt = "\nEnter `quit` to end the program. "

message = ''

while message != 'quit' :
	message = input(prompt)
	print(message)

