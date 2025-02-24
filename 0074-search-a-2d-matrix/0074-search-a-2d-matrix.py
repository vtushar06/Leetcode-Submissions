class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        for i,lis in enumerate(matrix):
            if target>=lis[0] and target<=lis[len(lis)-1]:
                low,high=0,len(lis)-1
                while(low<=high):
                    mid=(low+high)//2
                    if lis[mid]==target:
                        return True
                    elif lis[mid]>target:
                        high-=1
                    else:
                        low+=1   
        return False        
        