#Purpose : Generates a square


#Written by Kenny Ng Wai Yu
#On 18/10/2022

class Square():

    def __init__(self):
        self._size = int(input("Enter the size of the pattern: "))

        if self._size < 2 or self._size > 20:
            print("The entered size should fall between 1 to 20")
            exit(0)

    def draw_pattern(self):

        for vertical in range(1, self._size + 1):

            for horizontal in range(1, self._size  + 1):

                if horizontal % 2 == 0:

                    print(":", end = "")

                elif str(vertical)[-1] == '0':
                    print (9, end = "")

                elif vertical < 10 :
                    print (vertical - 1, end = "")

                else:
                    number = vertical % 10
                    print (number - 1, end = "")

            print ("\n", end = "")

square = Square()
square.draw_pattern()
