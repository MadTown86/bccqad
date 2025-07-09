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
        
        pos_s, pos_p, state = len(s)-1, len(p)-1, 0

        while True:
            if pos_p < 0:
                break
            if pos_s < 0:
                break

            # General Switchboard
            if state == 0:
                if p[pos_p] == s[pos_s]:
                    pos_p -= 1
                    pos_s -= 1
                elif p[pos_p-1] != '.' and p[pos_p] == '*':
                    state = 1
                elif p[pos_p-1] == '.' and p[pos_p] == '*':
                    state = 3
                elif p[pos_p] == '.':
                    state = 2
                else:
                    state = 4
            # Asterisk Found Only
            if state == 1:
                element = p[pos_p-1]
                if s[pos_s] != element:
                    state = 0
                    pos_p -= 2
                else:
                    calc = pos_p - 2 == pos_s + 1
                    while not calc and pos_s >=  0:
                        if s[pos_s] == element:
                            pos_s -= 1
                        else:
                            state = 0
                            pos_p -= 2
                            break
                    state = 0
                    pos_p -= 2

            # Period Found Only
            if state == 2:
                pos_s -= 1
                pos_p -= 1

            # Period and Asterisk Found
            if state == 3:
                calc = pos_p + 1 == pos_s + 1
                while not calc and pos_s >= 0:
                    pos_s -= 1
                pos_p -= 2
            # Do I need?
            if state == 4:
                pass

        if pos_p == -1 and pos_s == -1:
            return True
        else:
            return False


        
class TheirSolution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = len(s) - 1, len(p) - 1
        return self.backtrack({}, s, p, i, j)

    def backtrack(self, cache, s, p, i, j):
        key = (i, j)
        if key in cache:
            return cache[key]

        if i == -1 and j == -1:
            cache[key] = True
            return True

        if i != -1 and j == -1:
            cache[key] = False
            return cache[key]

        if i == -1 and p[j] == '*':
            k = j
            while k != -1 and p[k] == '*':
                k -= 2
            
            if k == -1:
                cache[key] = True
                return cache[key]
            
            cache[key] = False
            return cache[key]
        
        if i == -1 and p[j] != '*':
            cache[key] = False
            return cache[key]

        if p[j] == '*':
            if self.backtrack(cache, s, p, i, j - 2):
                cache[key] = True
                return cache[key]
            
            if p[j - 1] == s[i] or p[j - 1] == '.':
                if self.backtrack(cache, s, p, i - 1, j):
                    cache[key] = True
                    return cache[key]
        
        if p[j] == '.' or s[i] == p[j]:
            if self.backtrack(cache, s, p, i - 1, j - 1):
                cache[key] = True
                return cache[key]

        cache[key] = False
        return cache[key]
                       
            
if __name__ == "__main__":
    S = Solution()
    # Old Inputs: 
    inputs = [('bbbba', '.*a*a'), ('a', 'ab*'), ('aaba', 'ab*a*c*a'), ('aa', 'a*'), ('aaa', 'ab*a*c*a'), ('aaa', 'a*a'), ('aa', 'a'), ('ab', '.*'), ('mississippi', 'mis*is*ip*.'), ('ab', '.*c'), ('aaa', 'aaaa'), ('aab', 'c*a*b')]
    for inp in inputs:
        print(S.isMatch(*inp))

                

            