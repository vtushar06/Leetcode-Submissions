class Solution:
    def defangIPaddr(self, address: str) -> str:
        st=""
        for i in range(len(address)):
            if address[i]==".":
                st+="[.]"

            else:
                st+=address[i]
        return st            
        