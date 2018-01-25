class Car():
	def __init__(self, make, model, year):
		"""initialized attributes own auto"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""get formatted description own auto"""
		long_name = str(self.year) + self.model + self.make
		return long_name.title()
		
	def read_omometer(self):
		"""print value counter odometer in miles"""
		print("This car has " + str(self.odometer_reading) + " miles on it!")
		
	def update_odometer(self, mileage):
		"""set value for odometer"""
		if mileage >= self.odometer_reading :
			self.omomenter_reading = mileage
		else
			print('You can\'t roll back on odometer!')
	
	def increment_odometer(self, miles):
		if miles > 0 :
			self.odomenter_reading += miles
		else
			print('You can\'t roll back on odometer!')
