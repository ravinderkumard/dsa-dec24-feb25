class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=1
        
        for i in range(n-1,-1,-1):
            for curr_amount in range(1,amount+1):

                skip = dp[i+1][curr_amount]
                take = 0
                if coins[i]<=curr_amount:
                    take = dp[i][curr_amount - coins[i]]
                
                dp[i][curr_amount] = take+skip
        
        return dp[0][amount]