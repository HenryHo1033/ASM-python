class Stock():

    def __init__(self):
        self.__rate = ""
        self.__rates = []

        for day in range(5):

            self.__rate = input(f"Enter YEN rate of day {day + 1} (HKD):")

            while not self.validate():
                self.__rate = input(f"Enter YEN rate of day {day + 1} (HKD):")

            self.__rates.append(float(self.__rate))


    def is_number(self):

        try:
            float(self.__rate)
            return True

        except:
            return False

    def validate(self):

        if len(self.__rate) == 0 or self.__rate.isspace():

            print ("The input is empty.")
            return False

        elif not self.is_number():

            print ("The rate is not a number.")
            return False

        elif float(self.__rate) <= 0:

            print ("The rate should not be negative or zero.")
            return False

        else:
            return True

    def maximum(self):

        return max(self.__rates)

    def minimum(self):

        return min(self.__rates)

    def average(self):

        return sum(self.__rates) / len(self.__rates)

    def show_advice(self):

        print (f"The highest rate is {self.maximum()}")
        print (f"The lowest rate is {self.minimum()}")
        print (f"The average rate is {self.average()}")

        if self.average() - self.__rates[4] / self.__rates[4] > 0.15:

            return "BUY"

        elif self.average() - self.__rates[4] / self.__rates[4] > 0.15:

            return "SELL"

        else:

            return "HOLD"

stock = Stock()
print (stock.show_advice())