
params = "50.4,22.3,12,-2,45,82,123.5,-12,35"
params2 = [1,23,4,5,6,78,8]

def validate(params):

    if isinstance(params, str) is False:

        raise ValueError("Params is not String")

def process_cslist(params):

    validate(params)

    numbers = params.split(",")
    numbers = list(map(float,numbers))

    return sum(numbers) / len(numbers)

print (process_cslist(params))
print (process_cslist(params2))