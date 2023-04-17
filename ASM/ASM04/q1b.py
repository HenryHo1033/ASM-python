#Purpose :  application of the data structure of stack.

#Written by Kenny Ng Wai Yu
#On 17/4/2024
#For Assignment 4

def checkBalancedSymbols(exp):

    stack = []
    opening = set('([{')
    closing = set(')]}')
    matching = {'(': ')', '[': ']', '{': '}'}
    ignore = False  # Flag to ignore # symbol and anything after it

    for char in exp:
        if char == '#':
            ignore = True  # Set ignore flag to True when # symbol is encountered
        if ignore:
            continue  # Ignore everything after # symbol
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            last_open = stack.pop()
            if char != matching[last_open]:
                return False

    return not stack


print (checkBalancedSymbols('[1+(2-3)]'))
print (checkBalancedSymbols('{2 + [1+(2-3)]'))
print (checkBalancedSymbols('{2 + [1+(2-3)]} # ignored[[['))
print (checkBalancedSymbols('{2 + [1+(2-3)]} [[['))