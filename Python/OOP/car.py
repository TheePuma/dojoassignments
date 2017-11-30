class Car(object):
	def __init__(self, year, make, price, speed, fuel, mileage):
		self.year = year
		self.make = make
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 12
	def taxation(self):
		if self.price > 10000:
			self.tax = 15
			# print("Tax on this vehicle is at {}  of listed price.".format(self.tax))
			return self
		else:
			print("Tax on this vehicle is at {} of listed price.".format(self.tax))
			return self
	def display_all(self):
		self.taxation()
		print("Year: {}\nMake: {}\nPrice: {}\nTop Speed: {}\nFuel Type: {}\nMileage: {}\nTax: {}""%".format(self.year,self.make,self.price,self.speed,self.fuel,self.mileage,self.tax))
		return self
carrera = Car(2017,"Porsche", 100000, 190, "gas", 0)
belair = Car(1957,"Chevy", 30000, 160, "gas", 20000)
h1 = Car(1997, "Hummer", 250000, 70, "diesel", 5000)
carrera.display_all()
h1.display_all()
belair.display_all()