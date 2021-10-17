from typing import List


class Solution:
    def containsDuplicate(self, nums:List[int]) -> bool:
        temp = set()
        n = len(nums)
        for i in range(n):
            if nums[i]  in temp:
                return True
            temp.add(nums[i])
        return False

# list1 = [1, 2, 3, 1]
# # list2 = [1, 1, 2]
# print(Solution().containsDuplicate(list1))
