class dog():
	"""docstring for dog"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(f"{self.name.title()} is now sitting.")

	def roll_over(self):
		print(f"{self.name.title()} rolled over!")

my_dog = dog('willie', 6)
my_dog.sit()
my_dog.roll_over()
print("---")

class car():
	"""docstring for car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can not roll back an odometer!!!")

my_new_car = car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#changing data in atribute
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#changing data by method
my_new_car.update_odometer(21)
my_new_car.read_odometer()
print("---")

