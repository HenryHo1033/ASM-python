#Purpose : reads in the radius of the marble and then prints out the price.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Mables():

	def __init__(self):
		self._pi = 3.14159
		self._radius = 0
		self._quantity = 0
		self._volume = 0

	def radius(self):

		self._radius = float(input("Enter the radius(mm): "))

	def quantiy(self):

		self._quantity = int(input("Enter the quantity: "))

	def volume(self):

		self.radius()
		self.quantiy()
		self._volume = 4/3 * self._pi * self._radius ** 3

	def total_price(self):

		print ("Tailor-made marbles")
		self.volume()
		return format(self._volume * self._quantity, ".1f")

print (f"The price is {Mables().total_price()}")