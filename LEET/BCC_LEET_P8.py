# https://leetcode.com/problems/string-to-integer-atoi/description/
# Difficulty: Medium
# Name: String to Integer (atoi)

# Solved June 15, 2025
# 40.82% Time
# 28.93% Space

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        s = s.lstrip() 
        num_bin = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        res = ''
        x = 0
        flag = False
        sign = False

        # loop through s, check values with s[x]
        for x in range(len(s)):
            if not flag:
                if s[x] == '-' or s[x] == '+':
                    flag = True
                    if s[x] == '-':
                        sign = True
                elif s[x] in num_bin:
                    res += s[x]
                    flag = True
                elif s[x] == ' ':
                    pass
                else:
                    return 0
            elif flag:
                if s[x] not in num_bin:
                    break
                else:
                    res += s[x]

        if not res:
            return 0
        if int(res) >= (2**31):
            if sign:
                return -(2**31)
            else:
                return 2**31-1
        return int(res) if not sign else -int(res) 
    
class TheBestSolution:
    """
    DFA - new thing to study...yay...
    Deterministic Finite Automation
    """
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value

if __name__ == "__main__":
    S = Solution()
    inputs = [("42", 42), ("  -042", -42), ("0-1", 0), ("words and 987", 0), ("-900words and 987", 0), ("-1", 1)]
    for pair in inputs:
        print(S.myAtoi(pair[0]))
