"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1. 

思路：
1.建立一个无重复的字典，包含arr里所有的无重复元素
2.对每一个字典中的index，遍历arr
3.每当有一个值与该inddx相等，key的值加一
4.每个key的值相当于freq[index]
 """
from typing import List # 解决NameError: name 'List' is not defined

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        myTuple = tuple(arr) # 利用tuple的非重性
        myDictionary = {}
        for i in myTuple:
            myDictionary[i] = 0 #每个integer的初始freq为0
            for j in arr:
                if i == j:
                    myDictionary[i] += 1
        
        num = -1
        for i in myDictionary:
            if myDictionary[i] == i and i > num:
                num = myDictionary[i]

        return num


print(Solution().findLucky([1, 1, 2, 2]))

"""RESULT
Runtime: 264 ms, faster than 5.16% of Python3 online submissions for Find Lucky Integer in an Array.
Memory Usage: 14 MB, less than 44.71% of Python3 online submissions for Find Lucky Integer in an Array. 
 """