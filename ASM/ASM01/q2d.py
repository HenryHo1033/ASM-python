#Purpose : Uses a for loop to generate a lookup table for the square


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Square():

    def __init__(self):
        self._size = int(input("Enter the size of the pattern: "))

        if self._size < 2 or self._size >= 20:
            print("The entered size should fall between 1 to 20")
            exit(0)

    def draw_pattern(self):

        for vertical in range(1, self._size + 1):

            for horizontal in range(1, self._size  + 1):

                if horizontal == 1:

                    print("^", end = "")

                elif horizontal == self._size :

                    print("^", end = "\n")

                else:
                    print("$", end = "")


square = Square()
square.draw_pattern()
