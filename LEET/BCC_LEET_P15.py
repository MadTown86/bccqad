# https://leetcode.com/problems/3sum/description/
# Difficulty: Medium
# Name: 3Sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x, y, z = 0, 1, 2
        res = []
        nums.sort()

        calc = lambda x, y, z: nums[x] + nums[y] + nums[z] == 0
        add = lambda x, y, z: nums[x] + nums[y] + nums[z]

        if len(nums) == 3:
            if calc(x, y, z):
                return [nums]
            else:
                return []
            
        while x < len(nums)-2:
            if y >= len(nums) and z > len(nums):
                x += 1
                y = x + 1
                z = y + 1
                continue
            if z >= len(nums):
                y += 1
                z = y + 1
                continue
            elif calc(x, y, z):
                temp = [nums[x], nums[y], nums[z]]
                if temp not in res:
                    res.append([nums[x], nums[y], nums[z]])
                    z += 1
                else:
                    z += 1
            elif add(x, y, z) < 0 and z < len(nums):
                z += 1
            else:
                x += 1
                y = x + 1
                z = y + 1

        return res

        

if __name__ == "__main__":
    S = Solution()
    ans = [[[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]]
    inputs = [[2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10],[-2, 0, 1, 1, 2], [0, 0, 0, 0], [-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]
    for inp in inputs:
        print(S.threeSum(inp))