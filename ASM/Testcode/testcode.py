
from pyDequeStack import Stack

# MODIFY THE FUNCTION BELOW
def checkBalancedSymbols(exp):
    symbolStack = Stack()
    for ch in exp:
        if ch in ['[','(']:
            symbolStack.push(ch)
        elif ch in [']',')']:
            if symbolStack.isEmpty():
                return False
            chFromStack = symbolStack.pop()
            # Brackets must be of same type and match up
            if ch == ']' and chFromStack != '[' or \
                ch == ')' and chFromStack != '(':
                return False

    return symbolStack.isEmpty()



if __name__ == '__main__':
    exp = '[1+(2-3)]'
    print(checkBalancedSymbols(exp)) # should be True

    exp = '{2 + [1+(2-3)]'
    print(checkBalancedSymbols(exp)) # should be False

    exp = '{2 + [1+(2-3)]}'
    print(checkBalancedSymbols(exp)) # should be True

    exp = '{2 + [1+(2-3)]} # ignored'
    print(checkBalancedSymbols(exp)) # should be True

    exp = '{2 + [1+(2-3)]} # ignored[[['
    print(checkBalancedSymbols(exp)) # should be True

    exp = '{2 + [1+(2-3)]} [[['
    print(checkBalancedSymbols(exp)) # should be False
