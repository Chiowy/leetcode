# Given an integer, convert it to a Roman number
""" 
V             5
X             10
L             50
C             100
D             500
M             1000 

基本思路：
1.与12不同，这里建立一个所有字母能够表达的组合字典
2.遍历字典(easy)
 """

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

""" RESULT
 Runtime: 52 ms, faster than 84.43% of Python3 online submissions for Integer to Roman.
Memory Usage: 14 MB, less than 35.68% of Python3 online submissions for Integer to Roman.
 """