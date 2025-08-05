#https://leetcode.com/problems/generate-parentheses/
# difficulty: Medium
# Name: Generate Parenthesis

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        x, y = 0, n-1
        o, c = '(', ')'

        def checker(s: str):
            cs = []
            x = 0
            while x < len(s):
                if s[x] == '(':
                    cs.append(s[x])
                    x += 1
                else:
                    if cs:
                        cs.pop()
                        x += 1
                    else:
                        return False
            return True if not cs else False

        # center uniform
        while x != y:
            