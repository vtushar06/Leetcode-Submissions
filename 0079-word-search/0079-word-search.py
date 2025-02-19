class Solution(object):
    def wordsearch(self,m,n,i,j,board,word,index):
        if index==len(word):
            return True
        if i<0 or j<0 or i>=m or j>=n  or board[i][j]!=word[index]:
            return False
        tempchar=board[i][j]
        board[i][j]="#"
        opt1=self.wordsearch(m,n,i+1,j,board,word,index+1) 
        opt2=self.wordsearch(m,n,i,j+1,board,word,index+1)    
        opt3=self.wordsearch(m,n,i-1,j,board,word,index+1)    
        opt4=self.wordsearch(m,n,i,j-1,board,word,index+1) 
        board[i][j]=tempchar     
        return opt1 or opt2 or opt3 or opt4   

    def exist(self, board, word):
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if(self.wordsearch(m,n,i,j,board,word,0)):
                        return True
        return False
