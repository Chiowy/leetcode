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
        # padding
        for row in grid:
            row.insert(0, 0)
            row.append(0)
        grid.insert(0, [0] * (len(grid) + 2))
        grid.append([0] * (len(grid) + 2))

        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid) - 1):
                # 考虑0的情况
                center = grid[i][j]
                if center != 0:
                    area += 2
                    mylist = [grid[i + 1][j], grid[i - 1][j], grid[i][j - 1], grid[i][j + 1]] 
                    for x in mylist:
                        if center > x: area += center - x 
                    
        return area
print(Solution().surfaceArea([[1,2],[3,4]]))

"""RESULT
Runtime: 177 ms, faster than 18.98% of Python3 online submissions for Surface Area of 3D Shapes.
Memory Usage: 14 MB, less than 25.93% of Python3 online submissions for Surface Area of 3D Shapes.
"""