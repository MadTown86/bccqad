# BCC - LEETCODE SERIES - P476
# Difficulty: Easy
# Link: https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        """
        https://wiki.python.org/moin/BitwiseOperators

        Leetcode problems tend to cover core programming topics in ever increasing difficulty and/or complexity.

        This one is telling the user 'learn about 2's compliment and bitwise numbers to solve'

        Verbal Explanation:
        1. Use  integer.bit_length() to get the amount of digits required to represent the original integer
        2. Use the number 1 because it has a 1 in the 0's place (important for representing positive or negative)
        3. 1 << zfill : shift the 1 located in 0's place to the left by the length of the necessary comparison.
        4. Because we are going to use XOR (^) operator this means when comparing the original integer to the mask, if
        the values being compared are the same then a zero is placed, if they are different a 1 is placed.  
        5. Now use XOR on the original integer input and the mask you created.
        """
        # 101 (zfill length = 3)
        zfill = num.bit_length() # XOR, 101 : 0010
        mask = (1 << zfill) - 1 # 0100 - 0111
        return num ^ mask
    
if __name__ == "__main__":
    S = Solution()
    print(S.findComplement(5))
    print(S.findComplement(1))