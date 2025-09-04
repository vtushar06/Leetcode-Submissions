class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for _ in range(n)]
        result=[]
        def isValid(row, col):
            # check column
            for i in range(row):
                if board[i][col] == "Q":
                    return False

            # check left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # check right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True
            
        def backtrack(row,board):
            if row==n:
                result.append(["".join(board[i]) for i in range(len(board))])
                return
            for col in range(n):
                if(isValid(row,col)):
                    board[row][col]='Q'
                    backtrack(row+1,board)
                    board[row][col]='.'
        backtrack(0,board)
        return result            


        