from Question1 import question1


if __name__ == '__main__':
    A, B = question1()
    C = []
    i = 0
    j = 0
    k = 0
    # Merging the two sorted list
    while i <= 1536:
        if A[j] < B[k]:
            C.append(A[j])
            j += 1
            if j == 512:
                for remaining_elements in range(k, len(B)):
                    C.append(B[remaining_elements])
                break
        else:
            C.append(B[k])
            k += 1
            if k == 1024:
                for remaining_elements in range(j, len(A)):
                    C.append(A[remaining_elements])
                break
        i += 1
    print("Sorted List C:")
    print(C)
