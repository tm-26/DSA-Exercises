from Input import checkifint


if __name__ == '__main__':
    # Variable Deceleration
    temp = 0
    A = []
    j = 0
    i = 0

    print("Enter the individual numbers of your array, note the individual numbers need to be in the range of 1 to "
          "1024 (-1 to exit)")

    while temp != -1:
        print("Element #{}) ".format(j + 1), end='')
        temp = checkifint()
        if temp == -1:
            break
        A.append(temp)
        if A[j] < 1 or A[j] > 1024:
            print("Please enter a number from 1 to 1024")
            del A[j]
        else:
            j += 1
    productoflist = []

    for a in A:
        for b in A:
            if a != b:
                productoflist.append([])
                productoflist[i].append(a)
                productoflist[i].append(b)
                productoflist[i].append(a*b)
                i += 1

    # Start Printing Process
    print("All the 2-pairs of integers with the same product:")
    for list1 in productoflist:
        for list2 in productoflist:
            if list1[2] == list2[2] and list1[0] != list2[0] and list1[0] != list2[1] and list1[1] != list2[0] \
                    and list1[1] != list2[1]:
                print(f"{list1[0]} * {list1[1]} = {list2[0]} * {list2[1]}")
