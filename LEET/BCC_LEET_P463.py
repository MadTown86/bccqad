# BCC LEET P463
# https://leetcode.com/problems/island-perimeter/
# Solved - 5/10/2025
from typing import List


class MySolution:
    """
    Additive approach.
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    # Plan to check outer bounds at two points, easier to store values and visualize
                    left = j - 1
                    right = j + 1
                    up = i - 1
                    down = i + 1
                    
                    # Checking Outer Bounds and Adding to Perimeter
                    if up < 0:
                        res += 1
                    if down > len(grid) - 1:
                        res += 1
                    if left < 0:
                        res += 1
                    if right > len(grid[i]) - 1:
                        res += 1
                    
                    # UP
                    if up > -1 and grid[up][j] == 0:
                        res += 1
                    
                    # DOWN
                    if down < len(grid) and grid[down][j] == 0:
                        res += 1

                    # LEFT
                    if left > -1 and grid[i][left] == 0:
                        res += 1

                    # RIGHT
                    if right < len(grid[i]) and grid[i][right] == 0:
                        res += 1
        return res
    
class MostUpVotedSolution:
    """
    https://leetcode.com/problems/island-perimeter/solutions/5039036/faster-lesser-2-methods-detailed-approach-counting-dfs-python-java-c/
    
    Subtractive approach
    """
    def S2(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    #This accounts for all 'out-of-bounds' edges
                    perimeter += 4
                    # Always checking upper location except for when r = 0
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    # Always checking left location except for when c = 0
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter
        

    



        

if __name__ == "__main__":
    s1 = MySolution()
    s1.islandPerimeter([      [0, 1, 0, 0],     # [(0, 0), (0, 1), (0, 2), (0, 3)]
                              [1, 1, 1, 0],     # [(1, 0), (1, 1), (1, 2), (1, 3)]
                              [0, 1, 0, 0],     # [(2, 0), (2, 1), (2, 2), (2, 3)]
                              [1, 1, 0, 0]])    # [(3, 0), (3, 1), (3, 2), (3, 3)]

    s = MostUpVotedSolution()
    print(s.S2([              [0, 1, 0, 0],
                              [1, 1, 1, 0],
                              [0, 1, 0, 0],
                              [1, 1, 0, 0]]))  # Output: 16
    
    # print(s.islandPerimeter([[1]]))
    # print(s.islandPerimeter([[1,0]]))
    
