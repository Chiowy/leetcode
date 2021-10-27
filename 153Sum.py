# 2021/10/27 Wednsday

# 15.3Sum
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()#排序
        temp = []
        
        if len(nums) < 3:
            return temp

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                head, tail = i + 1, len(nums) - 1
                while head < tail:
                    while head < tail and nums[head] == nums[head+1]:
                        head = head + 1
                    if head-1 > i and nums[i] + nums[head] + nums[head-1] == 0:
                        temp.append([nums[i], nums[head], nums[head-1]])
                        head = head + 1
                        continue
                    while head < tail and  nums[tail] == nums[tail-1]:
                        tail = tail -1
                    if tail < len(nums) - 1 and nums[i] + nums[tail] + nums[tail+1] == 0:
                        temp.append([nums[i], nums[tail], nums[tail+1]])
                        tail -= tail
                        continue
                    if nums[i] + nums[head] + nums[tail] == 0:
                        temp.append([nums[i], nums[head], nums[tail]])
                        tail = tail - 1
                        head = head + 1
                    elif nums[i] + nums[head] + nums[tail] > 0:
                        tail = tail - 1
                    else:
                        head = head + 1
                    

        return temp

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()
#         ans = list()
        
        # # 枚举 a
        # for first in range(n):
        #     # 需要和上一次枚举的数不相同
        #     if first > 0 and nums[first] == nums[first - 1]:
        #         continue
        #     # c 对应的指针初始指向数组的最右端
        #     third = n - 1
        #     target = -nums[first]
        #     # 枚举 b
        #     for second in range(first + 1, n):
        #         # 需要和上一次枚举的数不相同
        #         if second > first + 1 and nums[second] == nums[second - 1]:
        #             continue
        #         # 需要保证 b 的指针在 c 的指针的左侧
        #         while second < third and nums[second] + nums[third] > target:
        #             third -= 1
        #         # 如果指针重合，随着 b 后续的增加
        #         # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
        #         if second == third:
        #             break
        #         if nums[second] + nums[third] == target:
        #             ans.append([nums[first], nums[second], nums[third]])
        
        # return ans


print(Solution().threeSum([-1,0,1,0]))
