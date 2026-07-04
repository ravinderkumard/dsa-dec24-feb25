class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[0])
        n = len(pairs)
        memo = [[None]*(n+1) for _ in range(n)]
        def longest(curr,prev):
            if curr == len(pairs):
                return 0
            if memo[curr][prev+1] is not None:
                return memo[curr][prev+1]

            take = 0
            if prev==-1 or pairs[prev][1]<pairs[curr][0]:
                take = 1+longest(curr+1,curr)
            not_take = longest(curr+1,prev)
            memo[curr][prev+1] = max(take,not_take)
            return max(take,not_take)

        return longest(0,-1)