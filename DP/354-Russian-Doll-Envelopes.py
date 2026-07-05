class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0],-x[1]))
        n = len(envelopes)
        memo = [[None]*(n+1) for _ in range(n)]
        def longest(curr,prev):
            if curr == n:
                return 0
            if memo[curr][prev+1] is not None:
                return memo[curr][prev+1]
            take = 0
            if prev == -1 or envelopes[prev][1]<envelopes[curr][1]:
                take = 1+longest(curr+1,curr)
            not_take = longest(curr+1,prev)
            ans = max(take, not_take)
            memo[curr][prev+1] = ans
            return ans

        return longest(0,-1)