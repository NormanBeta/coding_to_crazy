

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, n, board, res):
            if row == n - 1:
                res.append(''.join(board))
            for i in range(n):
                if islegal(row, i, board):
                    board[row][i] = 'Q'
                    backtrack(row + 1, n, board, res)
                    board[row][i] = '.'
            return res

        def islegal(row, col, board):
            # dui
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # xiedui
            i = row - 1
            j = col - 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # zong
            i = row - 1
            while i >= 0:
                if board[i][col] == 'Q':
                    return False
                i -= 1
            return True

        board = [['.' for i in range(n)] for i in range(n)]
        res = []
        backtrack(0, n, board, res)
        return res


def islegal(row, col, board):
    print(board[row][col])
    n = 4
    # dui
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        print(board[i][j])
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    # xiedui
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        print(board[i][j])
        print([i,j])
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    # zong
    i = row - 1
    while i >= 0:
        print(board[i][j])
        if board[i][col] == 'Q':
            return False
        i -= 1
    return True

