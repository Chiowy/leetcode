class Solution:
    def romanToInt(self, s: str) -> int:
        ls = []
        num = 0
        temp = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        for i in range(len(s)):
            ls.append(temp[s[i]])
        for i in range(len(s)):
            if i == 0:
                num = ls[i]
            else:
                if ls[i] > ls[i-1]:
                    num = ls[i] - 2*ls[i-1] + num
                else:
                    num = ls[i] + num

        return num

print(Solution().romanToInt("MCMXCIV"))