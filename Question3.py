from Input import checkifint
from Input import checkifnum


if __name__ == '__main__':

    print("This program will tell which elements in your array are extreme and it will also check if your array is "
          "sorted")
    print("How many elements is your array going to contain")
    # Variable Declaration

    n = checkifint()  # Used for validation
    A = [0 for i in range(n)]
    B = []
    sorted = True
    i = 0
    j = 0

    print("Now enter the individual elements of your array")

    while j < n:
        print("Element #{}) ".format(j+1), end='')
        A[j] = checkifnum()
        j += 1

    while i < n:
        if 0 < i < n - 1 and (A[i - 1] < A[i] > A[i+1] or A[i - 1] > A[i] < A[i + 1]):
            B.append(A[i])
            sorted = False
        i += 1
    if sorted:
        print("SORTED")
    elif not sorted:
        print(B)
