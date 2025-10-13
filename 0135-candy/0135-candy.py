class Solution:
    def candy(self, rating: List[int]) -> int:
            n=len(rating)
            l_r=[1]*n
            r_l=[1]*n
            i,j=1,n-2
            while(i<n):
                if(rating[i-1]<rating[i]):
                    l_r[i]=l_r[i-1]+1
                if(rating[j+1]<rating[j]):
                    r_l[j]=r_l[j+1]+1
                i+=1
                j-=1
            count=0    
            for k in range(n):
                count+=max(l_r[k],r_l[k])
            return count