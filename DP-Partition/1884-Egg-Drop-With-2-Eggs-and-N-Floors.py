class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [0] * (n+1)

        for floors in range(1,n+1):
            dp[floors] = float('inf')
            for x in range(1,floors+1):
                broken = x-1
                survive = dp[floors-x]
                
                dp[floors] = min(dp[floors],1+max(broken,survive))
        
        return dp[n]