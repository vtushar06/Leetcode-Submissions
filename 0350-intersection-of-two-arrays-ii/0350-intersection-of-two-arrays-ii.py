class Solution(object):
    def intersect(self, nums1, nums2):
        new=[]
        for num in nums1:
            if num in nums2:
                new.append(num)
                nums2.remove(num)
        return(list(new))
        