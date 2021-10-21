class Solution:
    def intToRoman(self, num: int) -> str:
        temp = {1000:'M', 900:'CM', 500:'D', 400:'CD',100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman = ''
        while num != 0:
            for i in temp:
                if i <= num:
                    num = num - i
                    roman = roman + temp[i]
                    break

        return roman

print(Solution().intToRoman(12))