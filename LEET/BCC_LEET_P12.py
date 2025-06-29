# https://leetcode.com/problems/integer-to-roman/
# Delifficulty: Medium
# Name: Integer to Roman

class MySolution:
    """
    Explicit, long-hand approach.

    time: 3ms - 79.16%
    space: 18.10 MB - 5.85%
    """
    def intToRoman(self, num: int) -> str:
        res = ''
        nums_set = num
        while nums_set > 0:
            if nums_set >= 1000:
                res += 'M'
                nums_set -= 1000
            elif nums_set >= 900:
                res += 'CM'
                nums_set -= 900
            elif nums_set >= 800:
                res += 'DCCC'
                nums_set -= 800
            elif nums_set >= 700:
                res += 'DCC'
                nums_set -= 700
            elif nums_set >= 600:
                res += 'DC'
                nums_set -= 600
            elif nums_set >= 500:
                res += 'D'
                nums_set -= 500
            elif nums_set >= 400:
                res += 'CD'
                nums_set -= 400
            elif nums_set >= 300:
                res += 'CCC'
                nums_set -= 300
            elif nums_set >= 200:
                res += 'CC'
                nums_set -= 200
            elif nums_set >= 100:
                res += 'C'
                nums_set -= 100
            elif nums_set >= 90:
                res += 'XC'
                nums_set -= 90
            elif nums_set >= 80:
                res += 'LXXX'
                nums_set -= 80
            elif nums_set >= 70:
                res += 'LXX'
                nums_set -= 70
            elif nums_set >= 60:
                res += 'LX'
                nums_set -= 60
            elif nums_set >= 50:
                res += 'L'
                nums_set -= 50
            elif nums_set >= 40:
                res += 'XL'
                nums_set -= 40
            elif nums_set >= 30:
                res += 'XXX'
                nums_set -= 30
            elif nums_set >= 20:
                res += 'XX'
                nums_set -= 20
            elif nums_set >= 10:
                res += 'X'
                nums_set -= 10
            elif nums_set >= 9:
                res += 'IX'
                nums_set -= 9
            elif nums_set >= 8:
                res += 'VIII'
                nums_set -= 8
            elif nums_set >= 7:
                res += 'VII'
                nums_set -= 7
            elif nums_set >= 6:
                res += 'VI'
                nums_set -= 6
            elif nums_set >= 5:
                res += 'V'
                nums_set -= 5
            elif nums_set >= 4:
                res += 'IV'
                nums_set -= 4
            elif nums_set >= 3:
                res += 'III'
                nums_set -= 3
            elif nums_set >= 2:
                res += 'II'
                nums_set -= 2
            elif nums_set >= 1:
                res += 'I'
                nums_set -= 1
            elif nums_set == 0:
                break
        return res

class TheirSolution:
    def intToRoman(self, num: int) -> str:
        i_to_r =  [(1000, 'M'), (900,'CM'), (500, 'D'), (400,'CD'), (100, 'C'),
            (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), 
            (5, 'V'), (4, 'IV'), (1, 'I')]
        r = ''
        for k,v in i_to_r:
            while k <= num:
                r += v
                num -= k
        return r     

        

if __name__ == "__main__":
    S = TheirSolution()
    inputs = [3749, 58, 1994]
    for inp in inputs:
        print(S.intToRoman(inp))
