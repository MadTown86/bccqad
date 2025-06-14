# https://leetcode.com/problems/reverse-integer/
# Difficulty: Medium
# Name: Reverse Integer

"""
Initial Thoughts:
1. Discussing digits and bit-length so most likely can be solved with bitwise operators
2. Restrained from using 64 bit integers - return 0
3. Dealing with 'signed' integers vs. unsigned.
"""

class Solution:
    def reverse(self, x: int) -> int:
        pass

if __name__ == "__main__":
    S = Solution()
    inp_ans = [(123, 321), (-123, -321), (120, 21)]
    for pair in range(len(inp_ans)):
        assert(S.reverse(inp_ans[pair][0]) == inp_ans[pair][1])

    