#Purpose : a list of numbers and return the multiple of only the negative numbers.
# function returns

#Written by Kenny Ng Wai Yu
#On 15/1/2023
#For Assignment 2

class MultNeg():


    def multNeg(self, numlist):

        multneg = None

        for item in numlist:
            try:
                number = int(item)
            except:
                return None

            if multneg is None and number < 0:
                multneg = number

            elif multneg is not None and number < 0:

                multneg *= number

            else:
                pass

        return multneg

#check Larger numlist
    def checkLarger(self, numlist, check):

        if len(numlist) == 0 or len(check) == 0:

            return False

        numlist_max = max(numlist)
        check_max = max(check)

        if check_max > numlist_max:

            return True


        else:

            return False

multneg_list = [
            [1, 2, 3, 4, 5, 0, -1, -2, -3, -4, -5],
            [-1, -2, -3, -4, -5, 0, 1, 2, 3, 4, 5],
            [-1, -2, -3, -4, -5],
            [],
            [0, 0, 0, 0, 0],
            [-1, -2, -3, -4, 'a'],
            [-1, -1],
            [-1, -1, -1]
           ]

check_numlist = [
    [],
    [1,2,3,4,5,6,7,8,9],
    [1,2,3,4,11]
]

check_checklist = [
    [1,2,3],
    [0, 0, 10],
    [0,0,10]
]

multneg = MultNeg()
print ("Test cases for multNeg(numlist):")
for i,l in enumerate(multneg_list):
    print (f"Test case {i + 1} :")
    print (f"data : {l}")
    print (f"return value: {multneg.multNeg(l)} \n")

print ("*" * 50)

print ("Test cases for checkLarger(numlist, check:)")

for i,l in enumerate(check_numlist):
    print (f"Test case {i + 1} :")
    print (f"numlist: {check_numlist[i]}, check: {check_checklist[i]}")
    print (f"return value: {multneg.checkLarger(*(check_numlist[i], check_checklist[i]))} \n")
