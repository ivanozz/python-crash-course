from car import Car

class ElectricCar(Car):
	"""descripted specific properties electrocar's"""
	
	def __init__(self, make, model, year):
		"""initiated parent's class properties"""
		super().__init__(make, model, year)
		self.battery = Battery()
		
class Battery() :
	"""simple model battery"""
	
	def __init__(self, battery_size=70):
		"""initiated attributes battery"""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""print info about battery this car"""
		print("This car has a " + str(self.battery_size) + "-kWh battery!")

	def get_range(self):
		""" get approximately lenght path for this car with current value battery"""
		
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		else :
			range = 0
			
		message = "This car can go approximately " + str(range)
		message += " miles on a full charge"
