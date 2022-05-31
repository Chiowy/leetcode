"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order
find two numbers such that they add up to a specific target number
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for point1 in range(len(numbers) - 1):
            head = point1 + 1
            tail = len(numbers) - 1
            while head <= tail:
                mid = (head + tail) // 2
                if numbers[mid] == target - numbers[point1]:
                    return [point1 + 1, mid + 1]
                elif numbers[mid] < target - numbers[point1]:
                    head = mid + 1
                else:
                    tail = mid - 1
                
            

print(Solution().twoSum([3,24,50,79,88,150,345], 200))
