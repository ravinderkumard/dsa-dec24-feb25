class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for curr in range(1,amount+1):
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr],dp[curr-coin]+1)

        return -1 if dp[amount]==amount+1 else dp[amount]