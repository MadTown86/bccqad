# https://leetcode.com/problems/4sum/description/
# Difficulty: Medium
# Name: 4Sum
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        TIME: 5.05%
        SPACE: 56.56%
        """
        res = []
        nums.sort()

        if len(res) == 4 and nums[a] + nums[b] + nums[c] + nums[d] == target:
            return nums
        elif len(res) == 4:
            return []

        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a+1, len(nums)-2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = len(nums)-1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    temp = [nums[a], nums[b], nums[c], nums[d]]
                    if temp not in res and s == target:
                        res.append(temp)
                        c += 1
                        d -= 1
                        while c + 1 < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d - 1 and nums[d] == nums[d + 1]:
                            d -= 1
                    elif s < target:
                        c += 1
                    else:
                        d -= 1
                    
        return res
    

class TheirSolution:
    """
    Very fast in comparison to mine.
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # skip duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                # skip duplicate starting values
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res


#Fastest Solution By A LARGE margin
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Pruning: If the smallest possible sum is greater than target, break early
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Pruning: If the largest sum with current i is less than target, skip
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # Similar pruning
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return results

if __name__ == "__main__":
    S = Solution()
    # STORE:  
    inputs = [([-3,-2,-1,0,0,1,2,3], 0), ([-3,-1,0,2,4,5], 2), ([-3,-1,0,2,4,5], 1), ([1,0,-1,0,-2,2], 0), ([2, 2, 2, 2, 2], 8)]
    for inp in inputs:
        print(S.fourSum(*inp))
