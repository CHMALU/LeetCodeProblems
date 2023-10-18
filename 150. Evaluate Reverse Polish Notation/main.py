def evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) -> int:
    prev_number = []

    for i, char in enumerate(tokens):
        if char not in ['+', '-', '*', '/']:
            prev_number.append(int(char))
        else:
            if char == '+':
                prev_number[-2] += prev_number[-1]
            elif char == '-':
                prev_number[-2] -= prev_number[-1]
            elif char == '*':
                prev_number[-2] *= prev_number[-1]
            elif char == '/':
                prev_number[-2] = int(prev_number[-2] / prev_number[-1])
            prev_number.pop()

    return prev_number[0] if len(prev_number) == 1 else False


print(evalRPN(tokens=["2", "1", "+", "3", "*"]))
print(evalRPN(tokens=["4", "13", "5", "/", "+"]))
print(evalRPN())
