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
        INT_MIN = -2**31
        INT_MAX = 2**31-1
        if INT_MIN < x < INT_MAX:
            minus_sign = True if x < 0 else False
            reversed = int(str(abs(x))[::-1])
            if INT_MIN < reversed < INT_MAX:
                if minus_sign:
                    return reversed * -1
                else:
                    return reversed
            else:
                return 0
        else:
            return 0
        
class BestSolution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])
        
        if res > 2 ** 31 - 1 or res < -2 ** 31:
            return 0
        
        return res


if __name__ == "__main__":
    S = Solution()
    inp_ans = [(123, 321), (-123, -321), (120, 21), (1534236469, 0)]
    print(S.reverse(inp_ans[3][0]))

    