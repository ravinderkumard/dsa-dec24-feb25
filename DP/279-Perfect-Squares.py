class Solution:
    # Time limit Exceed
    def numSquares(self, n: int) -> int:
        def solve(x):
            if x==0:
                return 0
            
            ans = float("inf")
            j = 1
            while j*j<=x:
                square = j*j
                ans = min(ans,1+solve(x-square))
                j+=1
            
            return ans
        
        return solve(n)

        