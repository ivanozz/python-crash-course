# передача произвольного числа аргументов
def make_pizza(*toppings) :
	"""вывод списка дополнений"""
	print(toppings)
	
# передача произвольного числа именованных аргументво
def build_profile(first, last, **userinfo) :
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	
	for key, value in userinfo.items() :
		profile[key] = value
	
	return profile
	
user_profile = build_profile('albert', 'einst', location='pricenton', field='physics')
