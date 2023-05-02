#Purpose : Use a while loop structure to print the savings after each number of months.


#Written by Kenny Ng Wai Yu
#On 18/10/2022

import time

class Savings():

        def __init__(self):

                self._savings = 10000
                self._increase = 0.15
                self._months = 0

                self._target = float(input("Enter target ($):"))

        def  saving(self):

                while self._savings < self._target:

                        self._savings = self._savings + self._savings * self._increase
                        self._months += 1

                        print (f"After {self._months} months saving is ${format(self._savings, '.2f')}:")
                        time.sleep(0.5)

                print (f"Reached ${self._target} after {self._months} months")

savings = Savings()
savings.saving()