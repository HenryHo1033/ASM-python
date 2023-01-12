
class Discount():

    def __init__(self):
        self.__gpa = ""

        while not self.validate():
            self.__gpa = input("Enter GPA: ")
            continue


    def is_number(self):

        try:
            float(self.__gpa)
            return True

        except:
            return False


    def validate(self):

        if len(self.__gpa) == 0 or self.__gpa.isspace():

            print ("The input is empty")
            return False

        elif not self.is_number():

            print ("The input is not a number")
            return False

        elif float(self.__gpa) < 0:

            print ("The GPA should not be negative")
            return False

        elif float(self.__gpa) < 2 or float(self.__gpa) > 4:

            print ("The GPA should be >=2.0 and <=4.0" )
            return False

        else:
            return True

    def discount_price(self):

        self.__gpa = float(self.__gpa)

        if self.__gpa >= 3.5:

            return 30

        elif self.__gpa >= 3 and self.__gpa < 3.5:

            return 31

        elif self.__gpa >= 2.5 and self.__gpa < 3:

            return 32

        else:

            return 33

    def show_price(self):

        print (f"The price is ${self.discount_price()}")

discount = Discount()
discount.show_price()