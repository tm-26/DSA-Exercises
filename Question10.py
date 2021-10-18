from Input import getintlist


def largestNum(list, length):
    if length == 1:
        return list[0]
    return max(list[length - 1], largestNum(list, length - 1))  # Recurse here


if __name__ == '__main__':
    A = getintlist()
    length = len(A)
    ans = largestNum(A, length)
    print(f"Largest element in your list --> {ans}")
