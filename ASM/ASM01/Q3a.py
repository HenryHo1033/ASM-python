#Purpose : Check the data collected over a period


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class IndexChecker():

    def __init__(self):

        self._day = 1
        self._days = 0
        self._uv_index = []
        self._sum = 0

    def average(self):

        for index in self._uv_index:

            self._sum += index

        return self._sum / len(self._uv_index)

    def maximum(self):

        return max(self._uv_index)

    def minimum(self):

        return min(self._uv_index)

    def extreme_uv_index(self):

        count = 0

        for index in self._uv_index:
            if index > 11:
                count += 1

        return count

    def low_uv_index(self):

        count = 0

        for index in self._uv_index:
            if index >= 0 and index <= 2:
                count += 1

        return count

    def higher_previous_day(self):

        count = 0

        for index in range (1, len(self._uv_index)):

            if self._uv_index[index] > self._uv_index[index - 1]:
                count += 1

        return count

    def checker(self):

        print ("UV Index Checker")
        self._days = int(input("Enter number of days of the UV index data collection period: "))

        while self._day <= self._days:

            input_validate = float(input(f"Enter the daily UV index of day {self._day}: "))

            if input_validate < 0 or input_validate > 25:
                print ("Input Error: UV index should be between 0 and 25 ")
                continue

            else:
                self._uv_index.append(input_validate)
                self._day += 1

    def report(self):

        self.checker()

        print (f"Average daily UV index in the period: {self.average()}")
        print (f"Maximum daily UV index is {self.maximum()}")
        print (f"Minimum daily UV index is {self.minimum()}")
        print (f"Number of days with Extreme UV index is {self.extreme_uv_index()}")
        print (f"Number of days with Low UV index is {self.low_uv_index()}")
        print (f"Number of days with UV index higher than previous day is {self.higher_previous_day()}")

IndexChecker().report()