class Solution:
    # Tabulation
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = [float('inf')]*(n+1)
        memo[n] = 0

        for i in range(n-1,-1,-1):

            j=i
            while j<n and days[j]<days[i]+1:
                j+=1
            
            cost1 = costs[0]+memo[j]

            j=i
            while j<n and days[j]<days[i]+7:
                j+=1
            cost7 = costs[1]+memo[j]

            j=i
            while j<n and days[j]<days[i]+30:
                j+=1
            cost30 = costs[2] + memo[j]

            memo[i] = min(cost1,cost7,cost30)
        return memo[0]
        