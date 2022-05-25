"""
let's call an arr a mountain if the following properties hold:
1. arr.length >= 3
2. there exists some i with 0 < i < arr.length -1 like:
    - arr[0] < arr[1] < ... < arr[i-1] < arr[i]
    - arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given a mountain arr that is guaranteed to be a mountain, return any i 

基本思路：
1. 二分查找
2. 取中位数为x，若x小于前（后）一个数，则二分前（后）一个数组
3. 直到x是不小于先后两个数
"""
from typing import List # 解决NameError: name 'List' is not defined
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        head = 0
        tail = len(arr) - 1
        
        mid = (head + tail) // 2
        while(arr[mid] < arr[mid + 1] or arr[mid] < arr[mid - 1]):
            mid = (head + tail) // 2
            if arr[mid] < arr[mid + 1]:
                head = mid
            if arr[mid] < arr[mid - 1]:
                tail = mid

        return mid

print(Solution().peakIndexInMountainArray([3, 4, 5, 1]))
"""RESULT
Runtime: 125 ms, faster than 26.45% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.6 MB, less than 19.53% of Python3 online submissions for Peak Index in a Mountain Array.
"""

