# BCC LEETCODE SERIES - P495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/description/
# Easy
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        damage = 0
        while timeSeries:
            sec = timeSeries.pop(0)
            # Last attack always takes full duration
            if not timeSeries:
                damage += duration
                break
            else:
                # Calculate the time between attacks
                distance = timeSeries[0] - sec
                if distance >= duration:
                    damage += duration # Take full damage
                else:
                    damage += duration - abs(duration - distance) # Take shortened damage based on distance.
        return damage
    
class FasterSolution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = 0
        # setting an initial previous always higher than duration to preserve first use of (i-prev)
        prev = -timeSeries[0] - duration
        # Looping through items directly, reduces need to 'creation' of a separate looping mechanism such as range(len)
        for i in timeSeries:
            # Add full duration
            res += duration
            # if current time plus (subtracting a negative) previous time and duration is less than duration 
            if i-prev < duration: res -= (duration - (i - prev))
            prev = i
        return res

if __name__ == "__main__":
    inputs = [([1, 4], 2), ([1, 2], 2), ([1, 4, 5, 9, 10], 2), ([1, 2, 3, 4, 5], 5)]
    ans = [4, 3, 8, 9]
    s = FasterSolution()
    for index in range(len(inputs)):
        # print(f'{s.findPoisonedDuration(*inputs[index])} :::: {ans[index]}')
        print(s.findPoisonedDuration(*inputs[index]) == ans[index])