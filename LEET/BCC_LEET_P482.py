# BCC LEETCODE SERIES - P482 - License Key Formatting
# https://leetcode.com/problems/license-key-formatting/description/
# Not a good showing on my part.  Took 9 submissions...

class MySolution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        if len(s) == 1 and s[0] != '-':
            return s.upper()
        x = 0
        first_group = (len(s) - s.count('-')) % k
        res = ''
        k_count = 0
        while x < len(s): 
            while len(res) <= first_group and first_group>0:
                if s[x] == '-':
                    x += 1
                elif len(res) == first_group:
                    res += '-'
                    break
                else:
                    res += s[x].upper()
                    x += 1
            if s[x] == '-':
                x += 1
            elif k_count < k:
                res += s[x].upper()
                k_count += 1
                x += 1
            elif k_count == k:
                res += '-'
                k_count = 0

        return res
    
class MostUpvoted:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        # https://leetcode.com/problems/license-key-formatting/solutions/540266/python-js-c-o-n-by-string-operation-w-explanation/
        # Eliminate all dashes
        S = S.replace('-', '')
        
        head = len(S) % K
        
        grouping = []
        
        # Special handle for first group
        if head:
            grouping.append( S[:head] )
        
        # General case:
        for index in range(head, len(S), K ):
            grouping.append( S[ index : index+K ] )
        
        
        # Link each group togetger and separated by dash '-'
        return '-'.join( grouping ).upper()


if __name__ == "__main__":
    S = MySolution()
    inp1 = ("5F3Z-2e-9-w", 4)
    inp2 = ("2-5g-3-J", 2)
    inp3 = ("2-4A0r7-4k", 4)
    inp4 = ("2-4A0r7-4k", 3)
    inp5 = ("2", 2)
    inp6 = ("a-a-a-a-", 1)
    inp7 = ("a0001afds-", 4)
    inp8 = ("--------EyRfCyHxyUJzhygiazYpjuDFdHvrnDwoQKQEsccLDiwhpmjueADIzqIvExbDDFnEGovAxYeszbzuTekRuWUPXRPbVKJuDQzIzzTj", 16)

    inputs = [inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8]
    ans = ["5F3Z-2E9W", "2-5G-3J", "24A0-R74K", "24-A0R-74K", "2", "A-A-A-A", "A-0001-AFDS", "EYRF-CYHXYUJZHYGIAZYP-JUDFDHVRNDWOQKQE-SCCLDIWHPMJUEADI-ZQIVEXBDDFNEGOVA-XYESZBZUTEKRUWUP-XRPBVKJUDQZIZZTJ"]
    for x in inputs:
        print(S.licenseKeyFormatting(*x) == ans[inputs.index(x)])
        