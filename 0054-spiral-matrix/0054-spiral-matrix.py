class Solution(object):
    def spiralOrder(self, matrix):
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1
        direction=0
        result=[]
        while(left<=right and top<=bottom and direction<4):
            if direction==0:
                for j in range(left, right + 1):
                    result.append(matrix[top][j])
                top += 1
            if direction ==1:
                for i in range(top, bottom + 1):
                    result.append(matrix[i][right])
                right -= 1   
            if direction==2:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])   
                bottom-=1     
            if direction==3:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
            direction=(direction+1)%4 
        return result                   