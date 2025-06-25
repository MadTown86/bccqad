# https://leetcode.com/problems/perfect-number/description/
# Difficulty: Easy
# Name: Perfect Number

import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        mid = int(math.sqrt(num))+1
        res = 1
        for x in range(2, mid):
            if num % x == 0:
                res+=x + num//x
        print(res)
        return res == num
    
class TheirSolution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        count=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                count+=i+num//i
        return num==count

if __name__ == "__main__":
    S = Solution()
    inputs = [7, 28, 120, 496, 8127]  
    for inp in inputs:
        print(S.checkPerfectNumber(inp))