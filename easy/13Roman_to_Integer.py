# Given a roman numeral, convert it to an integer
""" 
V             5
X             10
L             50
C             100
D             500
M             1000 
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        
        myDictionary = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 
                        'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}

        myList = []
        
        num = 0

        for i in range(len(s)):
            myList.append(myDictionary[s[i]])

        for i in range(len(s)):
            if i == 0:
                num = myList[i]
            else:
                if myList[i] > myList[i-1]:
                    num = myList[i] - 2*myList[i-1] + num
                else:
                    num = ls[i] + num

        return num

