class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        candidates.sort()
        def find(i,currsum,path):
            if currsum==target:
                result.append(path[:])
                return  
            if i>=len(candidates) or currsum>target:
                return
             
            path.append(candidates[i])
            find(i+1,currsum+candidates[i],path)
            path.pop()

            while(i+1<len(candidates) and candidates[i]==candidates[i+1]):
                i+=1
            find(i+1,currsum,path)    
                    


        find(0,0,[])
        return result    
        