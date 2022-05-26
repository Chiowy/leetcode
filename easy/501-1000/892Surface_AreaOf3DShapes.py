"""
-You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. 
-Each value v = grid[i][j] represents a tower of v cubes placed on top of cell (i, j).
-After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.
-Return the total surface area of the resulting shapes.
-Note: The bottom face of each shape counts toward its surface area.
"""

from typing import List # 解决NameError: name 'List' is not defined

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        for i in range(len(grid) - 1):
            for j in range(len(grid) - 1): #遍历矩阵
                if i == 0 or i == (len(grid) - 1):#第一行和最后一行的格子
                    if j == 0 or j == (len(grid) - 1):#四个角
                        area = area + grid[i][j] * 2

Solution().surfaceArea([[1, 2], [3, 4]])