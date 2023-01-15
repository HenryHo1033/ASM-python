#Purpose : generates K number of groups of N numbers

#Written by Kenny Ng Wai Yu
#On 15/1/2023
#For Assignment 2

import random

class RandomList():

#input check
    def __init__(self):

        self.__entries = int(input("Enter how many numbers are in each entry (N): "))

        while not self.n_validate():

            print("Please enter N numbers where 6 <= N <= 10.")
            self.__entries = int(input("Enter how many numbers are in each entry (N): "))


        self.__groups = int(input("Enter how many groups (K): "))

        while not self.k_validate():

            print("Please enter K numbers where 1 <= K <= 6.")
            self.__groups = int(input("Enter how many groups (K): "))


#value check
    def n_validate(self):

        if self.__entries < 6 or self.__entries > 10:

            return False

        else:

            return True

    def k_validate(self):

        if self.__groups < 1 or self.__groups > 6:

            return False

        else:

            return True

#random number
    def show_groups(self):

        for g in range(self.__groups):
            l = random.sample(range(100), self.__entries)

            print(l)

randomList = RandomList()
randomList.show_groups()