#https://leetcode.com/problems/longest-palindromic-substring/description/
# BCC LEETCODE SERIES P5 - LONGEST PALINDROMIC SUBSTRING
# MEDIUM

class MySolution:
    def longestPalindrome(self, s: str) -> str:
        palindromes = set()
        
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        if len(s) == 1 or len(s) == 0:
            return s

        # first set up cursor and seek
        cursor, right_seek, left_seek = 0, 1, 1
        while cursor < len(s):
            while right_seek < len(s):
                if s[right_seek] != s[cursor]:
                    right_seek += 1
                elif s[right_seek] == s[cursor] and right_seek == left_seek:
                    while right_seek < len(s) and s[right_seek] == s[cursor]:
                        right_seek += 1
                    if right_seek >= len(s):
                        palindromes.add(s[cursor:])
                    else:
                        palindromes.add(s[cursor:right_seek])
                elif s[right_seek] == s[cursor] and right_seek != left_seek:
                    stored_rightseek = right_seek
                    right_seek -= 1
                    while s[left_seek] == s[right_seek]:
                        if left_seek == right_seek:
                            if stored_rightseek + 1 >= len(s):   
                                palindromes.add(s[cursor:])
                            else:
                                palindromes.add(s[cursor:stored_rightseek+1])
                            break
                        elif left_seek > right_seek:
                            if stored_rightseek + 1 >= len(s):   
                                palindromes.add(s[cursor:])
                            else:
                                palindromes.add(s[cursor:stored_rightseek+1])
                            break
                        else:
                            left_seek += 1
                            right_seek -= 1
                    right_seek = stored_rightseek + 1
                    left_seek = cursor + 1
 
                else:
                    right_seek += 1
            cursor += 1
            right_seek = cursor + 1
            left_seek = cursor + 1
        if palindromes:
            return max(palindromes, key=len)
        else:
            return s[0]
        
class MyAttempt2:
    def longestPalindrome(self, s: str) -> str:

        max_length = 1
        max_string = s[0]

        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                if j-i+1 > max_length and s[i:j+1] == s[i:j+1][::-1]:
                    max_length = j-i+1
                    max_string = s[i:j+1]
                
        return max_string
    
class MyAttempt3:
    def longestPalindrome(self, s: str) -> str:
        max_l = 1
        max_s = s[0]

        # setup dp matrix for palindrome
        dp = [False for _ in range(len(s)) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > max_l:
                        max_l = i-j+1
                        max_s = s[j:i+1]

        return max_s

        
            






        
class TheirSolution1:
    """
    Expand Around Center
    https://leetcode.com/problems/longest-palindromic-substring/solutions/4212564/beats-96-49-5-different-approaches-brute-force-eac-dp-ma-recursion/
    """
    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str


class TheirSolution2:
    def longestPalindrome3(self, s: str) -> str:
        """Manacher's Algorithm"""
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str


if __name__ == "__main__":
    S = MyAttempt2()
    # "babad", "cbbd", "a", "aca", "xaabacxcabaaxcabaax", "ccc", "abcda", 
    inputs = ["tattarrattat"]
    for inp in inputs:
        print(S.longestPalindrome(inp))