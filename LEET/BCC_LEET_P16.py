# https://leetcode.com/problems/3sum-closest/
# Difficulty: Medium
# Name: 3Sum Closest

from typing import List
# import infinity  # Removed, use float('inf') instead

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        353ms - 51.8%
        17.75MB - 78.36%
        """
        
        res = float('inf') # Initial infinite placeholder to be replaced
        nums.sort() # sort array to use two pointers technique

        for x in range(len(nums)):
            y = x + 1
            z = len(nums)-1
            while y < z:
                s = nums[x] + nums[y] + nums[z]
                if s == target:
                    return s
                if abs(s - target) < abs(res - target):
                    res = s
                if s < target:
                    y += 1
                else:
                    z -= 1
        return res

            

if __name__ == "__main__":
    S = Solution()
    inputs = [([-1, 2, 1, -4], 1), ([0,0,0], 1)]

    for inp in inputs:
        print(S.threeSumClosest(*inp))