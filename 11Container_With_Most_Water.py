from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        tail = len(height) - 1
        head = max = v = h = w = 0
        while head < tail:
            w = tail - head
            if height[head] < height[tail]: 
                h = height[head]
                head = head + 1
            else:
                h = height[tail]
                tail = tail - 1
            
            v = h*w
            if v > max: max = v
        return max



testlist = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(testlist))