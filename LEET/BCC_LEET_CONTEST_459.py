from typing import List
from itertools import permutations
import math
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        nstr = str(n)
        dig_sum = 0
        mult_sum = 1
        for val in range(len(nstr)):
            dig_sum += int(nstr[val])

        for val in range(len(nstr)):
            mult_sum = mult_sum * int(nstr[val])

        if n % (dig_sum + mult_sum) == 0:
            return True
        else:
            return False

    def countTrapezoids(self, points: List[List[int]]) -> int:
        combos_s = [x for x in permutations(points, 4)]
        combos = combos_s
        res = 0
        slope_bin = []
        def slopeit(a, b):
            rise = a[0] - b[0]
            run = a[1] - b[1]
            return [rise, run]
        for x in range(len(combos)):
            combo = combos_s[x]
            line_1 = slopeit(combo[0], combo[1])
            line_2 = slopeit(combo[1], combo[2])
            line_3 = slopeit(combo[2], combo[3])
            line_4 = slopeit(combo[3], combo[0])
            slopes = [line_1, line_2, line_3, line_4]
            s1 = sum([x[0] for x in slopes])
            s2 = sum([x[1] for x in slopes])
            slope_bin.append(slopes)

            if s1 == 0 and s2 == 0 and [x[1] for x in slopes].count(0) == 2:
                res.append(slopes)


        for index in range(len(slope_bin)):
            print(f'Combo {combos_s[index]} ::: Slope {slope_bin[index]}')

        
        return res

from collections import defaultdict
class TheirSolution:
    """
    I didn't need to try to find all the slopes, find all pairs of unique horizontal lines
    and you have a unique horizontal trapezoid.
    """
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 1000000007
        groups = defaultdict(int)
        for _, y in points:
            groups[y] += 1
        res = total = 0
        for y, count in groups.items():
            lines = count * (count - 1) // 2
            res = (res + total * lines) % MOD
            total = (total + lines) % MOD
        return res



if __name__ == "__main__":
    S = Solution()
    inputs_1 = [99, 23]
    inputs_2 = [([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]])]
    for inp in inputs_2:
        print(S.countTrapezoids(inp))