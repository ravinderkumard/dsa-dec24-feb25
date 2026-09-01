class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        max_val = [[0]*n for _ in range(n)]

        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i+1,n):
                max_val[i][j] = max(max_val[i][j-1],arr[j])
        dp = [[0]*n for _ in range(n)]

        for length in range(2,n+1):
            for l in range(n-length+1):
                r = l+length-1

                dp[l][r] = float("inf")
                for k in range(l,r):
                    left_max = max_val[l][k]
                    right_max = max_val[k+1][r]
                    cost = dp[l][k]+dp[k+1][r]+left_max*right_max

                    dp[l][r] = min(cost,dp[l][r])
        
        return dp[0][n-1]


        # def solve(l,r):
        #     if l==r:
        #         return 0
            
        #     if (l,r) in memo:
        #         return memo[(l,r)]
        #     ans = float("inf")

        #     for k in range(l,r):
        #         left_cost = solve(l,k)
        #         right_cost = solve(k+1,r)

        #         left_max = max_val[l][k]
        #         right_max = max_val[k+1][r]

        #         root_cost = left_max * right_max
        #         total = left_cost+right_cost+root_cost

        #         ans = min(ans,total)
        #     memo[(l,r)] = ans
        #     return memo[(l,r)]
        
        return solve(0,n-1)
        