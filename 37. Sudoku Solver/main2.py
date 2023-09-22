import collections
import copy


class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        response = []

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[row//3, col//3]:
                        return False

                    cols[col].add(board[row][col])
                    rows[row].add(board[row][col])
                    squares[row//3, col//3].add(board[row][col])

        def Backtrcking(row, col):
            if row == 9:
                response.append((copy.deepcopy(board)))
                return

            new_col = (col + 1) % 9
            new_row = row + (col + 1)//9

            if board[row][col] == '.':
                for number in range(1, 10):
                    if str(number) not in rows[row] and str(number) not in cols[col] and str(number) not in squares[row//3, col//3]:
                        rows[row].add(str(number))
                        cols[col].add(str(number))
                        squares[row//3, col//3].add(str(number))
                        board[row][col] = str(number)

                        Backtrcking(new_row, new_col)

                        rows[row].remove(str(number))
                        cols[col].remove(str(number))
                        squares[row//3, col//3].remove(str(number))
                        board[row][col] = '.'
            else:
                Backtrcking(new_row, new_col)

        Backtrcking(0, 0)
        print(len(response))
        return response


obiekt = Solution()
print(obiekt.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
