# 2021/10/23 
# Saturday


from typing import List
import sys

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        left = int((m + n + 1) / 2)
        right = int((m + n + 2) / 2)

        return (self.findKth(nums1, 0, nums2, 0, left) + self.findKth(nums1, 0, nums2, 0, right)) / 2
    
    def findKth(self, nums1:List[int], i:int, nums2:List[int], j:int, k:int) -> int:
        if i>= len(nums1): 
            return nums2[j + k -1 ] #nums1为空数组
        if j >= len(nums2):
            return nums1[i + k - 1] #nums2为空数组
        if k == 1:
            return min(nums1[i], nums2[j])      

        if i + int(k/2) - 1 < len(nums1): midVal1 = nums1[i + int(k/2) - 1]
        else: midVal1 = sys.maxsize
        if j + int(k/2) - 1 < len(nums2): midVal2 = nums2[j + int(k/2) - 1]
        else: midVal2 = sys.maxsize

        if midVal1 < midVal2:
            return self.findKth(nums1, i + int(k/2), nums2, j, k - int(k/2))
        else:
            return self.findKth(nums1, i, nums2, j + int(k/2), k - int(k/2))

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
#         # 当有数组为空时
#         if nums1 == []:
#             return self.returnMidNumber(nums2)[1]
#         if nums2 == []:
#             return self.returnMidNumber(nums1)[1]

#         mid1 = self.returnMidNumber(nums1)[0]
#         mid2 = int((len(nums1) + len(nums2))/2) - mid1 



#     # 找出数组中的中位数
#     # 返回一个数组
#     # 数组的第一位表示 奇数数组的中位坐标，偶数数组两个中位数中较小的坐标
#     def returnMidNumber(self, nums2:List[int]) -> List[int]:
#         if len(nums2)%2:
#                 return (len(nums2)/2 ,nums2[int(len(nums2)/2)])
#         else:
#                 return (len(nums2)/2 - 1, (nums2[int(len(nums2)/2)] + nums2[int(len(nums2)/2) + 1]) / 2)


        

l2 = []
l1 = [2,4,4,5,5,5]
print(Solution().findMedianSortedArrays(l1, l2))


