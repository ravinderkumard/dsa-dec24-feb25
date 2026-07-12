class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)

        next_row = [0]*(n+1)

        for idx1 in range(n-1,-1,-1):
            curr_row = [0]*(n+1)
            for idx2 in range(n-1,-1,-1):
                if s[idx1]==rev[idx2]:
                    curr_row[idx2] = 1+next_row[idx2+1]
                else:
                    curr_row[idx2] = max(next_row[idx2],curr_row[idx2+1])
            next_row = curr_row
        
        return next_row[0]