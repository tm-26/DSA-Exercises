import Input

if __name__ == '__main__':
    print("Enter an arithmetic expression in RPN format so it can be evaluated")
    Expression = input()
    Elements = Expression.split()
    stack = []
    for i in range(len(Elements)):
        if Elements[i] == '+':
            stack[-2] = (stack[-2] + stack[-1])
            del stack[-1]
            print(f"Current Stack: {stack}")
        elif Elements[i] == '-':
            stack[-2] = (stack[-2] - stack[-1])
            del stack[-1]
            print(f"Current Stack: {stack}")
        elif Elements[i] == 'x':
            stack[-2] = (stack[-2] * stack[-1])
            del stack[-1]
            print(f"Current Stack: {stack}")
        elif Elements[i] == '/':
            stack[-2] = (stack[-2] / stack[-1])
            del stack[-1]
            print(f"Current Stack: {stack}")
        elif not Input.isint(Elements[i]):
            print(f"Error, {Elements[i]} is not a valid input")
            exit()
        else:
            stack.append(int(Elements[i]))
            print(f"Current Stack: {stack}")
    print(f"{Expression} = {stack[-1]}")
