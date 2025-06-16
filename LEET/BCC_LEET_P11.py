# https://leetcode.com/problems/container-with-most-water/
# Difficulty: Medium
# Name: Container With Most Water
from typing import List

class Solution:
    """
    TIME: 67ms - 92.21%
    SPACE: 28.44 MB - 67.35%
    """
    def maxArea(self, h: List[int]) -> int:
        x, y = 0, len(h)-1

        if len(h) == 2:
            return min(h[0], h[1])
        elif len(h) == 1:
            return 0
        highest = 0
        while x != y:
            calc = min(h[x], h[y]) * (y - x)
            if calc > highest:
                highest = calc
            if h[x] > h[y]:
                y -= 1
            else:
                x += 1
        return highest




if __name__ == "__main__":
    S = Solution()
    inputs = [[1, 8, 6, 2, 5, 4, 8, 3, 7], [1, 1]]
    with open("BCC_LEET_P11_INPUT.txt", 'r') as p:
        text = p.read()
        input_list = eval(text)
    print(S.maxArea(input_list))
