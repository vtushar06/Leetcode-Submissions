class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Step 1: remove leading whitespace
        if not s:
            return 0

        sign = 1
        i = 0

        # Step 2: handle sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        num = 0
        # Step 3: read digits
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Step 4: apply sign
        num *= sign

        # Step 5: clamp within 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num