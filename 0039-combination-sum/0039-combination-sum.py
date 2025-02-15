class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        def backtrack(index,path,currentsum):
            if currentsum==target:
                result.append(path[:])
                return
            if currentsum>target or index >= len(candidates):
                return

            path.append(candidates[index])
            backtrack(index,path,currentsum+candidates[index])
            path.pop()

            backtrack(index+1,path,currentsum)
        backtrack(0,[],0)
        return result            
        