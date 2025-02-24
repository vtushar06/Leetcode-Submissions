class Solution(object):
    def repairCars(self, ranks, cars):
        def timetaken(t):
            totalcars=0
            for r in ranks:
                n = int((t//r)**0.5)
                totalcars+=n
                if totalcars>=cars:
                    return True
            return False
           
        low=1
        high=min(ranks)*(cars**2)
        while low<high:
            mid=(low+high)//2
            if timetaken(mid):
                high=mid
            else:
                low=mid+1
        return low