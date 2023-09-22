import collections


class Solution(object):
    def isValidSudoku(self, board):
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    if board[x][y] in rows[y] or board[x][y] in cols[x] or board[x][y] in squares[x//3, y//3]:
                        return False

                    rows[y].add(board[x][y])
                    cols[x].add(board[x][y])
                    squares[x//3, y//3].add(board[x][y])

        return True


obiekt = Solution()
print(obiekt.isValidSudoku(board=[["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
