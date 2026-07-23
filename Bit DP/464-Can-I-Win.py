class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal<=0:
            return True
        
        total_value = (maxChoosableInteger*(maxChoosableInteger+1))//2
        if total_value<desiredTotal:
            return False
        memo = {}
        def dfs(mask,remaining):
            if (mask,remaining) in memo:
                return memo[(mask,remaining)]
            for num in range(1,maxChoosableInteger+1):
                bit = 1<<(num-1)
                if mask & bit:
                    continue

                if num >= remaining:
                    memo[(mask,remaining)] = True
                    return True
                if not dfs(mask|bit,remaining-num):
                    memo[(mask,remaining)] = True
                    return True
            memo[(mask,remaining)] = False
            return False

        return dfs(0,desiredTotal) 