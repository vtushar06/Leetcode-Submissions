class Solution(object):
    def romanToInt(self, s):
        def roman_to_int(s, index=0, total=0):
            roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
            if index >= len(s):  # Base case: if we reach the end of the string
                return total

            current_value = roman_map[s[index]]
    
            if index + 1 < len(s) and roman_map[s[index]] < roman_map[s[index + 1]]:
        # Subtraction case (e.g., IV, IX)
                return roman_to_int(s, index + 1, total - current_value)
            else:
        # Normal addition case
                return roman_to_int(s, index + 1, total + current_value)
        return roman_to_int(s)