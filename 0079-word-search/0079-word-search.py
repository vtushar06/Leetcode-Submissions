class Solution(object):
    direction=[[1,0],[0,1],[-1,0],[0,-1]]
    def find(self,i,j,index,board,word,m,n):
        
        if index==len(word):return True
        if i<0 or j<0 or i>=m or j>=n or board[i][j]!=word[index]:return False
        
        temp=board[i][j]
        board[i][j]="$"
        for dic in Solution.direction:
            new_i=i+dic[0]
            new_j=j+dic[1]
            if self.find(new_i,new_j,index+1,board,word,m,n):
                return True
        board[i][j]=temp
        return False       
    def exist(self, board, word):
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and self.find(i,j,0,board,word,m,n):
                    return True
        return False            

       
        