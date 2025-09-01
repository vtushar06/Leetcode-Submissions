class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def find(index,currsum,path):
            if currsum==target:
                result.append(path[:])
                return
            if currsum>target or index>=len(candidates):
                return
            # include that element and do not move
            path.append(candidates[index])
            find(index,currsum+candidates[index],path)
            # do not include that element and move 
            path.pop()
            find(index+1,currsum,path)  
            return
        find(0,0,[])
        return result    
        