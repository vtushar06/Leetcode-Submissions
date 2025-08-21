class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_freq = {}
        consonant_freq = {}
    
    # Count frequencies of vowels and consonants
        for char in s:
            if char in vowels:
                vowel_freq[char] = vowel_freq.get(char, 0) + 1
            else:
                consonant_freq[char] = consonant_freq.get(char, 0) + 1
    
    # Find maximum frequencies
        max_vowel_freq = max(vowel_freq.values()) if vowel_freq else 0
        max_consonant_freq = max(consonant_freq.values()) if consonant_freq else 0
    
        return max_vowel_freq + max_consonant_freq
        