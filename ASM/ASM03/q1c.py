import re

def isValidPassword(pwd):

    regex = re.compile("(?=.*\d)(?=.*[/*-+])[A-Za-z\d/*-+]{8,32}$")
    regex2 = re.compile("(?:88)")


    if len(pwd) < 8 or len(pwd) > 32:

        return False

    elif regex.search(pwd) is None:

        return False

    elif regex2.search(pwd) is None:

        return False

    else:

        return True

pwds = [        "12345678", #False
                "abcdefgh", #False
                "+-*/+-*/", #False
                "ABCDEFGH", #False
                "T9+-*/a", #False
                "1234567890+-*/88abcdefhYPINPk1gr" #False
                "T9+-*/a8", #False
                "T9+-/8a8", #False
                "T9+*/a88", #True
                "t9+*/a88", #True
                "1234567890+-*/88abcdefhYPINPk1gr"] #True


for pwd in pwds:

    print (isValidPassword(pwd))