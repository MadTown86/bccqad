# BCC_LEET_P647
# Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# Difficulty: Medium

#Questions To Ask Myself: 
# #   Can a binary matrix be filled and then iterated over to count total quantity of unique palindromes?


class Solution:
    def countSubstrings(self, s: str) -> int:
        res_qty = 1
        res_slice = s[0]

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i-j <= 2 or dp[i][j]):
                    dp[i][j] = True
