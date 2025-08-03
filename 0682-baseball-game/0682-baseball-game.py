class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i not in ("D", "+", "C"):
                stack.append(int(i))
            elif i=="D":
                last=stack[-1]
                stack.append(int(last*2))
            elif i=="C":
                stack.pop()
            else:
                last=int(stack[-1])
                secondlast=int(stack[-2])
                stack.append(last+secondlast)
        return sum(stack)