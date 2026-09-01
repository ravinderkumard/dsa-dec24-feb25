class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        max_val = [[0]*n for _ in range(n)]

        for i in range(n):
            max_val[i][i] = arr[i]
            for j in range(i+1,n):
                max_val[i][j] = max(max_val[i][j-1],arr[j])
        memo = {}
        def solve(l,r):
            if l==r:
                return 0
            
            if (l,r) in memo:
                return memo[(l,r)]
            ans = float("inf")

            for k in range(l,r):
                left_cost = solve(l,k)
                right_cost = solve(k+1,r)

                left_max = max_val[l][k]
                right_max = max_val[k+1][r]

                root_cost = left_max * right_max
                total = left_cost+right_cost+root_cost

                ans = min(ans,total)
            memo[(l,r)] = ans
            return memo[(l,r)]
        
        return solve(0,n-1)
        