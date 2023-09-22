def solveNQueens(n, m):
    column = set()
    positive = set()
    negative = set()
    response = []
    board = [['.'] * n for i in range(m)]

    def backtracking(row):
        if row == m:
            copy = ["".join(row) for row in board]
            response.append((copy))
            return

        for col in range(n):
            if col in column or (row+col) in positive or (row-col) in negative:
                continue

            column.add(col)
            positive.add(row+col)
            negative.add(row-col)
            board[row][col] = 'Q'

            backtracking(row+1)
            column.remove(col)
            positive.remove(row+col)
            negative.remove(row-col)
            board[row][col] = '.'

    backtracking(0)

    # for solution in response:
    #     for row in solution:
    #         print(row)
    #     print('')

    return response


print(solveNQueens(4, 4))
