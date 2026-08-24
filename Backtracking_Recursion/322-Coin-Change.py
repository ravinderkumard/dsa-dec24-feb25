class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-2]*(amount+1)
        
        def solve(amount):
            if amount ==0:
                return 0
            
            if amount < 0:
                return float('inf')
            
            if memo[amount]!=-2:
                return memo[amount]

            answer = float('inf')

            for coin in coins:
                result = solve(amount-coin)
                if result!=float('inf'):
                    answer = min(answer,result+1)
            memo[amount] = answer
            return answer
        
        result = solve(amount)
        return -1 if result==float('inf') else result
        