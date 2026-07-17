class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = len(stones)
        target = total//2
        dp = [[None] * (n) for _ in range(target+1)]
        def dfs(i,curr):
            if curr==0:
                return True
            if i == len(stones) or curr<0:
                return False
            
            if dp[curr][i] is not None:
                return dp[curr][i]
            
            take = dfs(i+1,curr-stones[i])
            skip = dfs(i+1,curr)
            dp[curr][i] = take or skip
            return take or skip

        for s in range(target,-1,-1):
            if dfs(0,s):
                return total-2*s
        return 0