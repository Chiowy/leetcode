"""
Given an integer n, return the number of structurally unique BST's (binary search trees) 
which has exactly n nodes of unique values from 1 to n.
"""

"""
假如，根结点为x
那么tree的左边有x-1个数，右边有n-x个数
对左半边，不同结构的数量可以递归为0到x-1的情况
对右半边而言，可以递归为x+1到n的情况

例如，n=5的情况
1. root 为 1，左边0个数，右边4个数
2. root 为 2，左边1个数，右边3个数
3. root 为 3，左边2个数，右边2个数
4，root 为 4，左边3个数，右边1个数
5. root 为 5，左边4个数，右边0个数
"""

class Solution:
    def numTrees(self, n: int) -> int:
        
