#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Difficulty = Medium
# Name: Letter Combinations of a Phone Number
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        TIME: 0ms, beats 100%?
        SPACE: 64.48%
        """
        if not digits:
            return []
        
        mapit = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        l_bin = []
        res = []
        l = len(digits)
        for x in digits:
            l_bin.append(mapit[x])
        
        if l == 1:
            for x in mapit[digits]:
                res.append(x)
        
        if l == 2:
            for x in range(len(l_bin[0])):
                for y in range(len(l_bin[1])):
                    res.append(l_bin[0][x] + l_bin[1][y])

        if l == 3:
            for x in range(len(l_bin[0])):
                for y in range(len(l_bin[1])):
                    for z in range(len(l_bin[2])):
                        res.append(l_bin[0][x] + l_bin[1][y] + l_bin[2][z])
        
        if l == 4:
            for x in range(len(l_bin[0])):
                for y in range(len(l_bin[1])):
                    for z in range(len(l_bin[2])):
                        for i in range(len(l_bin[3])):
                            res.append(l_bin[0][x] + l_bin[1][y] + l_bin[2][z] + l_bin[3][i])
        
        return res

class TopSolution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output

if __name__ == "__main__":
    S = TopSolution()
    inputs = ['23', '234', '2', '', '3']
    for inp in inputs:
        print(S.letterCombinations(inp))

        
        
        

