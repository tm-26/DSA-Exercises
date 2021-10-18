# TODO
# 1) Add Algorithms (Check)


from Input import checkifint
import math


def custom_method(number):
    if number <= 0:
        return False
    sqrt = math.floor(math.sqrt(number))
    numbers = [True for nums in range(sqrt+1)]
    i = 2
    while i < sqrt:
        if numbers[i]:
            if number % i == 0:
                return False
            else:
                for j in range(i * 2, sqrt + 1, i):
                    numbers[j] = False
                i += 1
        else:
            i += 1

    return True


def sieveoferatosthenes(number):
    if number <= 0:
        return False
    numbers = [True for i in range(number+1)]
    p = 2
    while p * p <= number:
        if numbers[p]:
            for i in range(p * 2, number + 1, p):
                numbers[i] = False
            if not numbers[number]:
                return False
        p += 1
    return True


if __name__ == '__main__':

    print("Find a prime number using:")
    print("1) A Custom Method")
    print("2) Sieve of Eratosthenes algorithm")
    exit = 0
    choice = 0
    while exit == 0:
        choice = checkifint()  # Validation
        if choice == 1:
            print("Enter an integer to check if it is prime")
            num = checkifint()
            ans = custom_method(num)
            if ans:
                print("Number is a prime!")
                exit += 1
            if not ans:
                print("Number is not a prime")
                exit += 1

        elif choice == 2:
            print("Enter a number to check if it is prime")
            num = checkifint()
            ans = sieveoferatosthenes(num)
            if ans:
                print("Number is a prime!")
                exit += 1
            if not ans:
                print("Number is not a prime")
                exit += 1
        else:
            print("Please enter a valid input")
