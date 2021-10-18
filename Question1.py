import random


def quick_sort(B):
    quick_sort2(B, 0, 1023)
    return B


def get_pivot(B, low, high):

    mid = (high + low) // 2
    pivot = high

    if B[low] < B[mid]:
        if B[mid] < B[high]:
            pivot = mid
        elif B[low] < B[high]:
            pivot = low
    return pivot


def partition(B, low, high):
    pivot_position = get_pivot(B, low, high)
    pivot_value = B[pivot_position]
    B[pivot_position], B[low] = B[low], B[pivot_position]
    border = low

    for i in range(low, high + 1):
        if B[i] < pivot_value:
            border += 1
            B[i], B[border] = B[border], B[i]
    B[low], B[border] = B[border], B[low]

    return border


def quick_sort2(B, low, high):
    if low < high:
        p = partition(B, low, high)
        quick_sort2(B, low, p - 1)
        quick_sort2(B, p + 1, high)


def question1():
    # Generate all the numbers to be sorted
    A = [int(random.random() * 1025) for i in range(512)]
    B = [int(random.random() * 1025) for i in range(1024)]
    # Print out the unsorted lists
    print("Unsorted List A")
    print(A)
    print("\n")
    print("Unsorted List B")
    print(B)
    print("\n")

    # Start of Shell Sort

    gap = 512 // 2

    while gap > 0:
        for i in range(gap, 512):
            temp = A[i]
            j = i
            while j >= gap and A[j - gap] > temp:
                A[j] = A[j - gap]
                j -= gap
            A[j] = temp
        gap //= 2

    # Start of Quick Sort

    B = quick_sort(B)
    return A, B


if __name__ == '__main__':

    A, B = question1()
    print("Sorted List A (Using Shell Sort)")
    print(A)
    print("\nSorted List B (Quick Sort)")
    print(B)
