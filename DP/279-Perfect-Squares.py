class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def solve(x):
            if x==0:
                return 0
            if x in memo:
                return memo[x]

            ans = float("inf")
            j = 1
            while j*j<=x:
                square = j*j
                ans = min(ans,1+solve(x-square))
                j+=1
            
            memo[x] = ans
            return ans
        
        return solve(n)

        