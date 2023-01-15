#Purpose : prints the square with apattern according to the examples below.

#Written by Kenny Ng Wai Yu
#On 15/1/2023
#For Assignment 2
class Square():

#Input
    def __init__(self):

        self.__size = input("Enter size of pattern: ")

        if self.validate(self.__size):

            self.__size = int(self.__size)

        else:

            raise Exception("Input number is not numeric.")

    def validate(self, size):

        return size.isnumeric()

    def print_pattern(self):

        for i in range(self.__size):
            for j in range(i, self.__size):

                    print(self.__size, end="")

            for k in range(self.__size):
                if k >= self.__size - i:
                    print("+", end="")

            print()


square = Square()
square.print_pattern()

