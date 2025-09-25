class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
            # If pattern length and number of words don't match → impossible
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        # Two hash maps: pattern → word and word → pattern
        char_to_word = {}
        word_to_char = {}
        
        for c, w in zip(pattern, words):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            else:
                char_to_word[c] = w
            
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False
            else:
                word_to_char[w] = c
        
        return True
        