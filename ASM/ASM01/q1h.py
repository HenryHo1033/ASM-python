#Purpose : Calculating the amount to pay for a customer ordering pens.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Pentype():

	def __init__(self):
		self._alltype = ["A", "B", "C"]
		self._allcolours = [1,2,4]
		self._total_price = 0

		print ("Pens ordering")
		self._type = input("Enter the required pen type (A, B, C) :")
		self._colour = int(input("Enter number of colours :"))
		self._number = int(input("Enter number of lots of 100 :"))

		if self._type not in self._alltype or self._colour not in self._allcolours or self._number <=0:
			print ("Error in the input")
			exit(0)

		if self._type == "A":
			self._type = {1 : 150, 2: 190, 4 : 260}

		elif self._type == "B":
			self._type = {1 : 110, 2: 130, 4 :170}

		else:
			self._type = {1 : 90, 2 : 100, 4 : 130}

	def total_price(self):

		self._total_price = self._type.get(self._colour) * self._number

	def amount(self):

		self.total_price()
		print (f"The amount to pay is ${self._total_price}")

Pentype().amount()