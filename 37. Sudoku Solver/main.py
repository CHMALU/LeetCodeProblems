import collections


class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        solved = False

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row//3, col//3]:
                        return solved

                    cols[col].add(board[row][col])
                    rows[row].add(board[row][col])
                    squares[row//3, col//3].add(board[row][col])

        def Backtracking(row, col):
            nonlocal solved
            if row == 9:
                solved = True
                return solved

            new_col = (col + 1) % 9
            new_row = row + (col+1) // 9

            if board[row][col] != ".":
                Backtracking(new_row, new_col)
            else:
                for number in range(1, 10):

                    if number not in rows[row] or number not in cols[col] or number not in squares[row//3, col//3]:
                        rows[row].add(number)
                        cols[col].add(number)
                        squares[row//3, col//3].add(number)
                        board[row][col] = str(number)

                        Backtracking(new_row, new_col)

                        if not solved:
                            rows[col].remove(number)
                            cols[row].remove(number)
                            squares[row//3, col//3].remove(number)
                            board[row][col] = '.'

        Backtracking(0, 0)
        return board


obiekt = Solution()
print(obiekt.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
