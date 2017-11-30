class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
		self.riding = False
	def ride(self):
		self.miles += 5
		print("Riding. Miles now {}.".format(self.miles))
		return self.miles
	def reverse(self):
		self.miles -= 5
		print ("Reversing. Miles now {}".format(self.miles))
		return self.miles
	def displayinfo(self):
		print ("Price: ${}. Tops out at {}mph. Total mile {}.".format(self.price, self.max_speed,self.miles))
		return self
harley = Bike(5000, 140, 1000)
harley.ride()
harley.displayinfo()
harley.reverse()