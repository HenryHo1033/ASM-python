
params = "50.4,22.3,12,-2,45,82,123.5,-12,35"
params2 = "50.4,22.3,12,-2,45,82,123.5,-12,35a"
params3 = [1,23,4,5,6,78,8]

def validate(cslist):

    if isinstance(cslist, str) is False:

        raise ValueError("Parameter is not a string")

def process_cslist(cslist):

    validate(cslist)

    numbers = cslist.split(",")

    for number in numbers:

        try:
            float(number)

        except:
            numbers.remove(number)

    numbers = list(map(float, numbers))

    return sum(numbers) / len(numbers)


print (process_cslist(params))
print (process_cslist(params2))
print (process_cslist(params3))