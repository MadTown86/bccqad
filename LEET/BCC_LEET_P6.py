# https://leetcode.com/problems/zigzag-conversion/description/
# Difficulty: Medium
# Name: Zigzag Conversion

class Solution:
    """
    634ms runtime
    34.35 MB space

    Not a great solution, but at least I could complete it without looking at the solutions.
    """
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) <= numRows or numRows == 1:
            return s

        spacing = numRows - 2 # Used to calculate initial matrix dimensions
        col_count = 0
        col_start = len(s)

        # spacing_count set-up for smaller input sizes

        if numRows == 3:
            spacing_count = 1
        elif numRows > 3:
            spacing_count = numRows - 2
        else:
            spacing_count = 0
        

        # Calculating required length for each row based on length of string input and numRows
        flag = True
        while col_start:
            if flag:
                if (col_start - numRows) >= 0:
                    col_start -= numRows
                    col_count += 1
                    flag = False
                elif -numRows < (col_start - numRows) < 0:
                    col_start -= numRows
                    col_count += 1
                    break
            else:
                if (col_start - spacing) >= 0:
                    col_start -= spacing
                    col_count += spacing
                    flag = True
                elif -spacing < (col_start - spacing) < 0:
                    col_count += col_start 
                    break
        
        # Building an empty array to populate
        # NOTE: You don't need to re-build it and waste memory space/time - you could just use a mathematical approach
        res = [[[] for x in range(col_count)] for x in range(numRows)]
        

        # Matrix input counters
        col_by_row = 0 # row per column
        col_count = 0 # what column you are currently on
        flag = True # Are you populating a 'full column' or a 'zag' 
        
        x = 0 # Counter/Index for string

        # Loop for filling res matrix
        while x < len(s):
            if flag: 
                # if you are populating a 'zig'
                if col_by_row < numRows:
                    res[col_by_row][col_count] = s[x]
                    col_by_row += 1
                    x += 1
                elif col_by_row >= numRows:
                    flag = False
                    col_count += 1
                    col_by_row = 0
            else:
                # if you are populating a 'zag'
                if spacing_count == 0:
                    flag = True
                    spacing_count = numRows -2 if numRows > 3 else 1 if numRows == 3 else 0

                elif 0 < spacing_count <= numRows - 2:
                    res[spacing_count][col_count] = s[x]
                    spacing_count -= 1
                    col_count += 1
                    x += 1

        string_res = ''
        for row in res:
            for col in row:
                string_res += col[0] if col else ''
        
        return string_res
    
class Solution2:
    """
    Beats 40% - Time Complexity O(n)
    Beats 90% - Memory Complexity O(n)
    """
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        l = len(s)

        if l <= numRows or numRows == 1:
            return s 
        
        sp = 0 if numRows < 3 else numRows - 2
        

        rc = 0
        sl = sp
        f = True
        x = 0
        while x < l:
            if f and rc < numRows:
                res[rc].append(s[x])
                rc += 1
                x += 1
            elif f and rc >= numRows:
                rc = 0
                f = False

            elif not f and sl > 0:
                res[sl].append(s[x])
                sl -= 1
                x += 1
            
            else:
                sl = sp
                f = True

        return ''.join(''.join(x) for x in res)
    
# https://leetcode.com/problems/zigzag-conversion/solutions/6146922/two-points-to-solve-the-question/
# Highest Upvote Python Solution

class ThierSolution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]

        for char in s:
            rows[idx].append(char)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)   
    
if __name__ == "__main__":
    S = Solution2()
    # ("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 5), ("AB", 1), ("ABC", 2),
    inputs = [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 5), ("AB", 1), ("ABC", 2), ("PAYPALISHIRING", 7)]

    for number, question  in enumerate(inputs):
        if number == 1:
            assert(S.convert(*question) == "PAHNAPLSIIGYIR")
        elif number == 2:
            assert(S.convert(*question) == "PINALSIGYAHRPI")
        else:
            print(S.convert(*question))
                
