class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # dp[k][r1][r2]
        dp = [[[-inf] * n for _ in range(n)] for _ in range(2 * n - 1)]

        dp[0][0][0] = grid[0][0]

        for k in range(1, 2 * n - 1):

            # possible row values at step k
            for r1 in range(max(0, k - (n - 1)), min(n, k + 1)):
                c1 = k - r1

                if grid[r1][c1] == -1:
                    continue

                for r2 in range(max(0, k - (n - 1)), min(n, k + 1)):
                    c2 = k - r2

                    if grid[r2][c2] == -1:
                        continue

                    cherries = grid[r1][c1]

                    if r1 != r2:
                        cherries += grid[r2][c2]

                    best = -inf

                    # both came from left
                    best = max(best, dp[k - 1][r1][r2])

                    # person1 from up
                    if r1 > 0:
                        best = max(best, dp[k - 1][r1 - 1][r2])

                    # person2 from up
                    if r2 > 0:
                        best = max(best, dp[k - 1][r1][r2 - 1])

                    # both from up
                    if r1 > 0 and r2 > 0:
                        best = max(best, dp[k - 1][r1 - 1][r2 - 1])

                    if best != -inf:
                        dp[k][r1][r2] = best + cherries

        return max(0, dp[2 * n - 2][n - 1][n - 1])