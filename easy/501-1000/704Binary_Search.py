from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2  # 二分
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:  # 取左半边
                tail = mid - 1  # 而不是tail = mid
            else:
                head = mid + 1  # 而不是head = mid
        return -1