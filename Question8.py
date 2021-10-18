from Input import checkifnum
from Input import checkifint

if __name__ == '__main__':
    print("Enter a number to find and approximation of it's root, using the Newton-Raphson method")
    n = checkifnum()  # Validation
    print("How many times would you like the algorithm to loop")
    loop = checkifint()  # Validation
    i = 0
    x = n / 2  # Initial guess
    if n < 0:
        print("Root of non-positive numbers cannot be found using the Newton-Raphson method")
        exit()
    while i < loop:
        x = 1/2 * (x + (n/x))
        print(f"Loop #{i+1} --> {x}")
        i += 1
