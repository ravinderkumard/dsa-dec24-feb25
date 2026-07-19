class Solution:
    def twoEggDrop(self, n: int) -> int:
        memo = {}

        def dfs(floors, eggs):
            if floors <= 1:
                return floors

            if eggs == 1:
                return floors

            if (floors,eggs) in memo:
                return memo[(floors,eggs)]

            ans = float("inf")

            for x in range(1, floors + 1):
                broken = x - 1
                survive = dfs(floors - x, eggs)

                ans = min(ans, 1 + max(broken, survive))
                
            memo[(floors,eggs)] = ans
            return ans

        return dfs(n, 2)