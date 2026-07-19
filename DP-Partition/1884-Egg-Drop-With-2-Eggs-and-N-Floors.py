class Solution:
    def twoEggDrop(self, n: int) -> int:
        dp = {}
        def dfs(eggs,floors):

            if eggs==1:
                return floors
            if floors<=1:
                return floors
            
            if (eggs,floors) in dp:
                return dp[(eggs,floors)]

            min_val = float("inf")
            for i in range(1,floors+1):
                if (eggs-1,i-1) in dp:
                    low = dp[(eggs-1,i-1)]
                else:
                    low = dfs(eggs-1,i-1)
                    dp[(eggs-1,i-1)] = low
                
                if (eggs,floors-i) in dp:
                    high = dp[(eggs,floors-i)]
                else:
                    high = dfs(eggs,floors-i)
                    dp[(eggs,floors-i)] = high 

                temp = 1+max(low,high)
                min_val = min(min_val,temp)
            dp[(eggs,floors)] = min_val
            return min_val
        
        return dfs(2,n)