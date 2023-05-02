#Purpose : Generates a square pattern


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Sequence():

	def __init__ (self, min, max):

		self._min = min
		self._max = max
		self._result = [ ]

	@property
	def sequence(self):
		return self._result

	@sequence.setter
	def sequence(self, addend):

		for number in range(self._min, self._max + 1, addend):

				self._result.append(number)

sequence1 = Sequence(1,17)
sequence1.sequence = 2

sequence2 = Sequence(4,68)
sequence2.sequence = 8

print (sequence1.sequence)
print (sequence2.sequence)