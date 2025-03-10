class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        c=0
        seen=set()
        for i in range(left,right+1):
            c+=1
            for j in range(len(ranges)):
                a=ranges[j]
                lr=a[0]
                rr=a[-1]
                if lr<=i<=rr:
                    seen.add(i)
        if len(seen)==(c)  :
            return True
        else:
            return False