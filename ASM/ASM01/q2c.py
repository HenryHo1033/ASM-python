#Purpose : Uses a for loop to generate a lookup table for the square


#Written by Kenny Ng Wai Yu
#On 18/10/2022

import math

class Lookup():

        def __init__(self):

                self._column1 = "N|".rjust(15, " ")
                self._column2 = "N^2|".rjust(15, " ")
                self._column3 = "N^1/2|".rjust(15, " ")
                self._column4 = "floor(N^1/2|".rjust(15, " ")
                self._column5 = "ceil(N^1/2|".rjust(15, " ")

        def  table_generate(self):

                print (self._column1,self._column2,self._column3,self._column4,self._column5)

                for number in range(1, 12+1):

                    num1 = str(number).rjust(15, " ")
                    num2 = format(math.pow(number, 2),'.2f').rjust(15," ")
                    num3 = format(math.pow(number, 1/2), '.2f').rjust(15, " ")
                    num4 = format(math.floor(math.pow(number, 1/2)), '.2f').rjust(15, " ")
                    num5 = format(math.ceil(math.pow(number,1/2)), '.2f').rjust(15, " ")

                    print (num1,num2,num3,num4,num5)

lookup = Lookup()
lookup.table_generate()

