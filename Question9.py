import Input


if __name__ == '__main__':
    print("Enter an array of integers to find any repeated integers")
    Numbers = Input.getintlist()  # Gets a list through Input file
    Frequency = {}
    # Puts a counter on all elements
    for i in Numbers:
        try:
            Frequency[i] += 1
        except:
            Frequency[i] = 1
    print("The repeated integers in your array are:")
    # All those elements that had a frequency that is larger then one, had to be repeated. hence we check for this
    # condition, and if the condition is true, that element is repeated.
    for i in Numbers:
        if Frequency[i] > 1:
            print(f"{i},", end="")
            Frequency[i] = 0  # To prevent the same element being printed out more then once
    print("\b ")  # To delete the last comma, as it is clearly redundant
