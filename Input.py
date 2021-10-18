"""""
This file sole's purpose is to get different kinds of inputs (such as lists) and to validate other inputs
"""


def isint(input):
    try:
        int(input)
        return True
    except ValueError:
        return False


def checkifint():
    num = 0
    exit = 0
    while exit == 0:
        try:
            num = int(input())
            exit += 1
        except ValueError:
            exit = 0
            print("Please enter an integer")
    return num


def checkifnum():
    num = 0
    exit = 0
    while exit == 0:
        try:
            num = float(input())
            exit += 1
        except ValueError:
            exit = 0
            print("Please enter a number")
    return num


def getintlist():
    exit = 0
    A = []
    i = 0
    print("Enter your individual integers (q) to exit")
    while exit == 0:
        i += 1
        print(f"Element #{i}")
        temp = input()
        if temp == 'q':
            exit += 1
        elif not isint(temp):
            print("Please enter an integer")
            i -= 1
        else:
            A.append(int(temp))
    return A
