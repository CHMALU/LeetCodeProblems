def generateParenthesis(n: int):
    stack = []
    result = []

    def backtracking(openN, closedN):
        if openN == closedN == n:
            result.append("".join(stack))
            return

        if openN < n:
            stack.append('(')
            backtracking(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            stack.append(')')
            backtracking(openN, closedN + 1)
            stack.pop()

    backtracking(0, 0)
    return result


print(generateParenthesis(3))
