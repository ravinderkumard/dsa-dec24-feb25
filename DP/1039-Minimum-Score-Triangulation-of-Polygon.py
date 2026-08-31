class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        memo = [[-1]*n for _ in range(n)]

        def dfs(i,j):
            if j-i<2:
                return 0
            if memo[i][j] != -1:
                return memo[i][j]
            answer = float("inf")
            for k in range(i+1,j):
                cost = dfs(i,k)+dfs(k,j)+values[i]*values[k]*values[j]
                answer = min(cost,answer)
            memo[i][j] = answer
            return answer
        
        return dfs(0,n-1)