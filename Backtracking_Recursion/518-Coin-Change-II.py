class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def backtrack(index,amount):
            if amount==0:
                return 1

            if index==len(coins) or amount<0:
                return 0

            if (index,amount) in memo:
                return memo[(index,amount)]

            take = backtrack(index,amount-coins[index])
            skip = backtrack(index+1,amount)
            memo[(index,amount)] = take+skip
            return take+skip
        
        return backtrack(0,amount)

        