#Purpose : rolls two dice of which one of the dice with the above defect,

#Written by Kenny Ng Wai Yu
#On 15/1/2023
#For Assignment 2
import random

class Counting():

#count
    def __init__(self):

        self.__dice1 = [1,2,3,4,5,6]
        self.__dice2 = [1,1,2,3,4,5]

        self.__sumCount = {
            "sum2" : 0,
            "sum3" : 0,
            "sum4" : 0,
            "sum5" : 0,
            "sum6" : 0,
            "sum7" : 0,
            "sum8" : 0,
            "sum9" : 0,
            "sum10" : 0,
            "sum11" : 0,
            "sum12" : 0
        }

        self.__sum = 0

    def counting(self):

        return self.__sumCount

    def rolling(self):

        self.randIndex1 = random.randint(0, 5)
        self.randIndex2 = random.randint(0, 5)

        return (self.randIndex1, self.randIndex2)

    def total_sum(self, randIndex):

        return sum((self.__dice1[randIndex[0]],self.__dice2[randIndex[1]]))

#count result
    def count(self):

        self.__sum = self.total_sum(self.rolling())


        if self.__sum == 2:

            self.__sumCount["sum2"] += 1

        elif self.__sum == 3:

            self.__sumCount["sum3"] += 1

        elif self.__sum == 4:

            self.__sumCount["sum4"] += 1

        elif self.__sum == 5:

            self.__sumCount["sum5"] += 1

        elif self.__sum == 6:

            self.__sumCount["sum6"] += 1

        elif self.__sum == 7:

            self.__sumCount["sum7"] += 1

        elif self.__sum == 8:

            self.__sumCount["sum8"] += 1

        elif self.__sum == 9:

            self.__sumCount["sum9"] += 1

        elif self.__sum == 10:

            self.__sumCount["sum10"] += 1

        elif self.__sum == 11:

            self.__sumCount["sum11"] += 1

        elif self.__sum == 12:

            self.__sumCount["sum12"] += 1

    def show_result(self, counting):

        print (f"Sum Freq")

        for count in counting:
            print('{:>2} {:>5} '.format(''.join(list(filter(str.isdigit, count))), counting[count])
                  , "+" * int(counting[count]/10))


counting = Counting()

for i in range(0,1000):

    counting.count()


counting.show_result(counting.counting)