#Purpose : Modify the program so that the new rule applies.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Counting():
	
	def __init__(self):

		self._unit_price = 12.5
		self._number = 0

	def number(self):

		self._number = int(input("Enter the number of signature bread: "))

	def total_price(self):

		self.number()

		if self._number >9 :

			return self._unit_price * self._number - self._unit_price

		else:

			return self._unit_price * self._number

print (f"Amount to pay is {format(Counting().total_price(), '.1f')}")