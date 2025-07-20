# https://leetcode.com/problems/3sum/description/
# Difficulty: Medium
# Name: 3Sum

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        The last one to be incremented leads the loop and becomes the 'base closing condition'
        """
        res = []
        if not nums:
            return []
        
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0:
                        temp = [nums[x], nums[y], nums[z]]
                        if temp not in res:
                            res.append(temp)
        return res
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        x, y, z = 0, 1, len(nums)-1
        res = []
        nums.sort()

        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue

            y = x + 1
            z = len(nums)-1

            while y < z:
                s = nums[x] + nums[y] + nums[z]
                temp = [nums[x], nums[y], nums[z]]

                if s > 0:
                    z -= 1
                elif s < 0:
                    y += 1
                else:
                    res.append(temp)
                    y += 1

                    while nums[y] == nums[y+1] and y < z:
                        y += 1

            return res    
        
class TheirSolution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # skips duplicate values at nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = len(nums) - 1

            # continue looping while j != k
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    #skip duplicate values at nums[j]
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        
        return res


if __name__ == "__main__":
    S = TheirSolution()
    try:
        with open('C:\\PYREPOS\\bccqad\\LEET\\BCC_LEET_P15_input.txt', 'r') as r:
            text = r.read()
            text = eval(text)
    except Exception as e:
        print(e)
    
    ans = [[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2], ]
    inputs = [[-1,0,1,2,-1,-4,-2,-3,3,0,4], [-2,-3,0,0,-2],[-4,-2, 1],[-1, 0, 1], [2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10], [-2, 0, 1, 1, 2], [0, 0, 0, 0], [-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0]]
    for inp in inputs:
        print(S.threeSum(inp))

