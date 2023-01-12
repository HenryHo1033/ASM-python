class Square():

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
                if j >= 10:
                    print("0", end="")

                else:
                    print(j, end="")

            for k in range(self.__size):
                if k >= self.__size - i:
                    print("+", end="")

            print()

square = Square()
square.print_pattern()