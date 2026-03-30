class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find the index of the first occurrence of the character
        idx = word.find(ch)
        
        # If the character is not found, return the original word
        if idx == -1:
            return word
        
        # Reverse the prefix up to the index (inclusive) and append the rest of the word
        return word[:idx+1][::-1] + word[idx+1:]