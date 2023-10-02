#Purpose : n prints out the data that has been entered in a specific format as shown below.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Ratings():
	def __init__(self):
		self._restaurant_name = input("Rate a restaurant \nEnter "
					"restaurant name: ")

		self._score = float(input("Enter score (0-10) for the restaurant: "))
	def output_msg(self):
		return f"Thank you for giving {format(self._score, '.2f')} scores to {self._restaurant_name} "

ratings = Ratings()
print (ratings.output_msg())		