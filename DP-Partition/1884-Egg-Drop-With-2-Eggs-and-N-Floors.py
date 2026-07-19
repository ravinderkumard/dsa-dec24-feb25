class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = [[-1] * 3 for _ in range(n+1)]

        def dfs(eggs,floors):

            if eggs==1:
                return floors
            if floors<=1:
                return floors
            
            if dp[floors][eggs]!=-1:
                return dp[floors][eggs]

            min_val = float("inf")
            for i in range(1,floors+1):
                if dp[i-1][eggs-1]!=-1:
                    low = dp[i-1][eggs-1]
                else:
                    low = dfs(eggs-1,i-1)
                    dp[i-1][eggs-1] = low
                
                if dp[floors-i][eggs]!=-1:
                    high = dp[floors-i][eggs]
                else:
                    high = dfs(eggs,floors-i)
                    dp[floors-i][eggs] = high 

                temp = 1+max(low,high)
                min_val = min(min_val,temp)
            dp[floors][eggs] = min_val
            return min_val
        
        return dfs(2,n)