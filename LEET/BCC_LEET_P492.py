# BCC - LEETCODE SERIES - P492 : Construct The Rectangle
# https://leetcode.com/problems/construct-the-rectangle/description/
# Easy
# First Try - Not Efficient

from typing import List
from collections import defaultdict

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        s = defaultdict(list)
        for l in range(1, area+1):
            if area % l == 0:
                w = int(area / l)
                if l >= w:
                    s[abs(l-w)] += [l, w]
        
        return s[min(s.keys())]
    
# Highest Upvotes Solution
# 
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for l in range(int(area**0.5), 0, -1): 
            """
            1. Finds 'true center' aka square-root of the number to split 
            2. Turn to integer and increment downward by 1 until you find the first factor of area that has no remainder.
            --automatically chooses closest possible L and W
            """  
            print(l)         
            if area % l == 0: 
                return [area // l, l]



        


if __name__ == "__main__":
    inputs = [4, 37, 122122]
    answers = [[2, 2], [37, 1], [427, 286]]

    s = Solution()
    print(s.constructRectangle(inputs[2]))
    