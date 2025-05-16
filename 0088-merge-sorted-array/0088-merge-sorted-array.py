class Solution:
    def merge(self, arr1: List[int], m: int, arr2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left1,left2=0,0
        newarr=[]

        while(left1<m and left2<n):
            if arr1[left1]<arr2[left2]:
                newarr.append(arr1[left1])
                left1+=1
            else:
                newarr.append(arr2[left2])
                left2+=1

        while left1<m:
            newarr.append(arr1[left1]) 
            left1+=1

        while left2<n:
            newarr.append(arr2[left2]) 
            left2+=1

    # Make sure it has enough space
        for i in range(m + n):
            arr1[i] = newarr[i]  

        