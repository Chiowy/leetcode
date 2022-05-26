"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order. 
基本思路：
1.双指针，第二个指针从第一个指针后面出发
2.两个指针对应的数的和为target，则结束
3.边界问题，数组长度要大于1，第一个指针不能在最后一个位置上(len(nums) > 1, point1 < len(nums) - 1)
 """
from typing import List # 解决NameError: name 'List' is not defined
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        LenOfNum = len(nums)
        if LenOfNum < 2:
            return "error"
        else:
            for point1 in range(0, LenOfNum - 1):
                for point2 in range(point1 + 1, LenOfNum):
                    if nums[point1] + nums[point2] == target:
                        return [point1, point2]

print(Solution().twoSum([1, 2, 4, 7, 3], 11))
""" RESULT
Runtime: 4895 ms, faster than 17.78% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 76.44% of Python3 online submissions for Two Sum. """
