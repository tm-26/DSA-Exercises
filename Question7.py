import Input
import sys
# Global Variable Decleration
binaryTree = []


def tree(input, i, index):

    if len(binaryTree) == 0:
        binaryTree.append({'index': index, 'num': int(input), 'left': 0.5, 'right': 0.5})
        return
    elif (binaryTree[index])['num'] >= input and (binaryTree[index])['left'] == 0.5:
        (binaryTree[index])['left'] = i
        binaryTree.append({'index': index, 'num': input, 'left': 0.5, 'right': 0.5})
        return
    elif (binaryTree[index])['num'] < input and (binaryTree[index])['right'] == 0.5:
        (binaryTree[index])['right'] = i
        binaryTree.append({'index': index, 'num': input, 'left': 0.5, 'right': 0.5})
        return
    elif (binaryTree[index])['num'] >= input:
        tree(input, i, binaryTree[index]['left'])
    elif (binaryTree[index])['num'] < input:
        tree(input, i, binaryTree[index]['right'])
    else:
        sys.exit("Error")


if __name__ == '__main__':
    exit = 0
    A = [0]
    i = 0
    print("Enter your individual number (q) to exit")
    while exit == 0:
        print(f"Element #{i}")
        temp = input()
        if temp == 'q':
            exit += 1
        elif not Input.isint(temp):
            print("Please enter an integer")
            i -= 1
        else:
            tree(int(temp), i, 0)
            i += 1
            print(binaryTree)
