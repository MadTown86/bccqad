# https://leetcode.com/problems/regular-expression-matching/description/
# Difficulty: HARD
# NAME: Regular Expression Matching

import re

class FirstSolution:
    """
    Time: 16.57%
    Space: 50.24%
    """
    def isMatch(self, s: str, p: str) -> bool:
        p = re.compile(p)
        matches = re.match(p, s)
        if matches:
            return True
        else:
            return False
        

from string import ascii_letters

class Solution:
    """
    DFA - This another case of the definite finite cases for string searching?
    """
    def isMatch(self, s: str, p: str) -> bool:
        """
        States::
        0 - char-for-char and switch_board
        1 - asterisk
        2 - period
        3 - period + asterisk?
        4 - ending-char-for-char
        """
        
        pos_d, pod_p, state = 0, 0, 0

        while pod_p <= len(p):
             
            if state == 0:
                if s[pos_d] == 




            
            
if __name__ == "__main__":
    S = Solution()
    # Old Inputs: ('aa', 'a'), ('aa', 'a*'), ('ab', '.*'), ('mississippi', 'mis*is*ip*.'), 
    inputs = [('ab', '.*c'), ('aaa', 'aaaa')]
    for inp in inputs:
        print(S.isMatch(*inp))

                

            