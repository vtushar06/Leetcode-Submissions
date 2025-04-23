class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            else:
                if len(stack)==0:return False
                char=stack.pop()
                if ((s[i]=="]" and char=="[") or  (s[i]=="}" and char=="{") or (s[i]==")" and char=="(")):
                    continue
                else:
                    return False
        return len(stack)==0                    
        