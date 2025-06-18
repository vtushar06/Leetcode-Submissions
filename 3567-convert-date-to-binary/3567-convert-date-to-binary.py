class Solution:
    def convertDateToBinary(self, date: str) -> str:
        year, month, day = date.split('-')
        # Convert each part to int, then to binary without leading zeroes or '0b' prefix
        year_bin = bin(int(year))[2:]
        month_bin = bin(int(month))[2:]
        day_bin = bin(int(day))[2:]
        return f"{year_bin}-{month_bin}-{day_bin}"
        