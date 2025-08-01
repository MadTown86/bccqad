# https://leetcode.com/problems/generate-parentheses/description/
# Difficulty: Medium
# Name: Generate Parentheses

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        s = '()'*n
        parse = [x for x in s]
        res = []
        res.append(s)
        front = 1
        back = float('inf')
        while front < back:
            back = len(s)-front-1
            parse[front] = '('
            parse[back] = ')'
            res.append(''.join(parse))
            front += 2
        
        return res

if __name__ == "__main__":
    S = Solution()
    inputs = [3, 1, 5, 6    ]
    for inp in inputs:
        print(S.generateParenthesis(inp))