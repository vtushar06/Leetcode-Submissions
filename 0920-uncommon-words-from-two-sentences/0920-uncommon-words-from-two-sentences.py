class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1 = s1.split()
        words2 = s2.split()
        
        # Count frequencies across both sentences
        counts = Counter(words1 + words2)
        
        # Collect words with frequency 1
        return [word for word, freq in counts.items() if freq == 1]