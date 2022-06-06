"""
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.
"""


class Solution:
    def numTrees(self, n):
        if n <= 1:
            return 1
        return sum(self.numTrees(i) * self.numTrees(n - 1 - i) for i in range(n))


print(Solution().numTrees(4))