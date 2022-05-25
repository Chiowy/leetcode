# Given a roman numeral, convert it to an integer
""" 
V             5
X             10
L             50
C             100
D             500
M             1000 

基本思路：
1.建立字典，输入根据字典映射到输出
2.在基础映射的基础上添加额外的规则，如果小的字母在大的字母的前面，这小字母和大字母构成一个组合，表示的integer为大减去小的
3.先遍历原始输出映射，再添加额外的规则
 """
class Solution:
    def romanToInt(self, s: str) -> int:
        
        """ myDictionary = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 
                        'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1} """
        myDictionary = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1} #建立字典
        myList = [] #建立原始映射表，目前为空
        
        num = 0

        for i in range(len(s)):
            myList.append(myDictionary[s[i]]) #第一次映射

        for i in range(len(s)): #遍历第一次映射
            if i == 0:
                num = myList[i] #初始值为第一个字母
            else:
                if myList[i] > myList[i-1]: # 从第二个字母开始，如果大于前一个，
                    num = myList[i] - 2*myList[i-1] + num #则加上之前所有的num，再减去两倍的前一个字母（basic math）
                else:
                    num = myList[i] + num  # 否则正常的加

        return num

print(Solution().romanToInt("MCMXCIV")) #test

""" RESULT
Runtime: 119 ms, faster than 5.10% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.9 MB, less than 76.93% of Python3 online submissions for Roman to Integer.
 """