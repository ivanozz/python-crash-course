def describe_pet(animal_type, pet_name = 'someone') :
	""" print info about animal """
	print('\nI have a ' + animal_type + '!')
	print('My ' + animal_type + '\'s name is '+pet_name.title()+'!')

describe_pet('hamster', 'harry')
#or
describe_pet(pet_name = 'harry', animal_type = 'hamster')
#or
describe_pet('dog')

# запрет изменения списка в функции
# т.е. передача в функцию копии спискаы
print_models(unprinted_designs[:], completed_models)
