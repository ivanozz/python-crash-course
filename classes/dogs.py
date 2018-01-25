class Dog():
	"""Простая модель собаки"""
	
	def __init__(self, name, age):
		"""Инициализирует атрибуты name и age"""
		self.name = name
		self.age = age
		
	def sit(self):
		"""Собака садится по команде"""
		print(self.name.title() + ' is now sitting.')
	
	def roll_over(self):
		"""Собака перекатывается по команде"""
		print(self.name.title() + ' rolled over!')

my_dog = Dog('willie', 6)
print(my_dog.name)
print(my_dog.age)
my_dog.sit()
my_dog.roll_over()
