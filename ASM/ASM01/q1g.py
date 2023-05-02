#Purpose : Calculate the final amount payable given the number of pizza slices.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Amount():

    def __init__(self):

        self._unit_price = 15
        self._unit_discount = 12
        self._amount = 0

        print ("Pizza take-away shop ")

        self._number = int(input("Enter the number of pizza slices: "))

        if self._number <= 0:

            print ("Sorry the input is not a valid input")
            exit(0)


    def total_price(self):

        self._amount = format(self._unit_price * self._number, '.1f')

    def discount_price(self, number):

        self._amount = format(6 * self._unit_price + number * self._unit_discount, '.1f')

        if float(self._amount) >= 200:

            self._amount = format(float(self._amount) * 0.85, '.1f')

    def amount(self):

        if self._number > 6:

            self.discount_price(self._number - 6)
            print (f"Amount to pay is ${self._amount}")

        else:
            self.total_price()
            print (f"Amount to pay is ${self._amount}")


Amount().amount()