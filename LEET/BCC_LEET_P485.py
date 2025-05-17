# https://leetcode.com/problems/max-consecutive-ones/description/
# BCC LEETCODE SERIES P 485
# EASY
# First Try - 31ms Runtime, 27.4 MB Memory

from typing import List

class MyFirstSolution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Not very fast or efficient because these two first checks are required with the way I am doing it.

        Also converting the original list of integers to strings consumes time, then splitting and then
        performing the len() built-in function at each iteration is adding to time and memory complexity.
        """
        if len(nums) == 1 and nums[0] == 1:
            return 1
        elif len(nums) == 1:
            return 0
        sNum = ''.join([str(x) for x in nums])
        sNum = sNum.split('0')
        print(sNum)
        highest = 0
        for item in sNum:
            if len(item) > highest:
                highest = len(item)
        return highest
    
class Solution(object): 
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi = result = 0
        
        for num in nums: # Direct iteration without translating information.
            if num == 1:
                result += 1
                maxi = max(maxi, result)
            else:
                result = 0
        return maxi

if __name__ == "__main__":
    S = MyFirstSolution()
    inputs = [[1,1,0,1,1,1], [1,0,1,1,0,1]]

    for inp in inputs:
        print(S.findMaxConsecutiveOnes(inp))