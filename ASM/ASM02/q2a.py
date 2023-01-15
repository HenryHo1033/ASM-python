#Purpose : A lucky draw

#Written by Kenny Ng Wai Yu
#On 15/1/2023
#For Assignment 2

import re

class LuckyDraw():

    def __init__(self):
        self.__regex = re.compile(r"[^A-Z\s]+")

        self.__cate_i = ["W", "E", "L", "C", "O", "M", " "]
        self.__cate_ii = ["T", "H", "A", "N", "K", "S", " "]

        self.__cate_i_count = 0
        self.__cate_ii_count = 0
        self.__cate_iii_count = 0

        self.__name = input("Please input your name to join the LuckyDraw.")

        while not self.validate():
            print("Your name must be CAPITAL or Space character, Please try again.")
            self.__name = input("Please input your name to join the LuckyDraw： ")


    def validate(self):

        if len(self.__regex.findall(self.__name)) != 0:

            return False

        else:

            return True

#Category check
    def char_count(self, name):

        for char in name:

            if char in self.__cate_i:

                self.__cate_i_count += 1

            elif char in self.__cate_ii:

                self.__cate_ii_count += 1

            else:

                self.__cate_iii_count += 1

#return value
    def isWinLuckyDraw(self):

        self.char_count(self.__name)

        if (self.__cate_iii_count > self.__cate_ii_count) and (self.__cate_i_count == 0):

            return True

        else:

            return False

draw = LuckyDraw()
print (draw.isWinLuckyDraw())