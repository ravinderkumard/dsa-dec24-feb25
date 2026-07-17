class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = len(stones)
        target = total//2

        dp = [[False]*(n+1) for _ in range(target+1)]
        for i in range(n+1):
            dp[0][i] = True
        
        for s in range(1,target+1):
            for i in range(n-1,-1,-1):
                dp[s][i] = dp[s][i+1]
                if s>=stones[i]:
                    dp[s][i] = dp[s][i] | dp[s-stones[i]][i+1]

        for s in range(target,-1,-1):
            if dp[s][0]:
                return total-2*s
        
        return 0