#Purpose : calculate the amount to pay given the number of “signature bread” in a purchase.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Counting():

	def __init__(self):

		self._unit_price = 12.5
		self._number = 0
		self._total_price = 0

	def number (self):

		self._number = float(input("Enter the number of signature bread: "))

	def total_price (self):

		self.number()
		self._total_price = self._unit_price * self._number
		return f"Amount to pat for 12 signature bread is {self._total_price}"

print (Counting().total_price())