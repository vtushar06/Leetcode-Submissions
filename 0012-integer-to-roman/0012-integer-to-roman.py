class Solution(object):
    def intToRoman(self, num):
        roman_map=[(1000,"M"),(900,"CM"),(500,"D"),
        (400,"CD"),(100,"C"),(90,"XC"),(50,"L"),
        (40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),
        (1,"I")]
        def convert(num,index=0):
            if num==0:return ""

            value,symbol=roman_map[index] 
            if num>=value:
                return symbol+convert(num-value,index)
            else:
                return convert(num,index+1)
        return convert(num)               