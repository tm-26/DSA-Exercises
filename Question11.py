from Input import checkifint
from Input import checkifnum
import math


def trigexpansion(num, choice, n):
    n = n-1
    i = 0
    final = 0
    if choice == 1:  # Sin Expansion
        while n > i:
            final = final + ((((-1) ** i) * num ** ((2 * i) + 1)) / (math.factorial((2 * i) + 1)))
            i += 1
        return final
    elif choice == 2:  # Cos Expansion
        while n > i:
            final = final + ((-1) ** i * num ** (2 * i)) / math.factorial(2 * i)
            i += 1
        return final
    else:
        return False


if __name__ == '__main__':
    print("Enter a number to apply a trigonometric function to")
    num = checkifnum()
    print("Select which function you wish to apply to your number")
    print("1) sin")
    print("2) cos")
    exit = 0
    choice = 0
    while exit == 0:
        choice = checkifint()
        if choice != 1 and choice != 2:
            print("Please enter either 1 or 2")
        else:
            exit += 1
    print("To how many terms of the series expansion would you like to compute")
    n = checkifint()
    ans = trigexpansion(num, choice, n)
    if choice == 1:
        print(f"sin({num}) = {ans}")
    else:
        print(f"cos({num}) {ans}")
