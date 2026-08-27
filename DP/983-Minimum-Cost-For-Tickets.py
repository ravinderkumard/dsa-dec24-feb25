class Solution:
    #Recursion + Memoization
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        memo = [float('inf')]*n
        def backtrack(idx):
            if idx==n:
                return 0
            if memo[idx]!=float('inf'):
                return memo[idx]

            j = idx
            while j<n and days[j]<days[idx]+1:
                j+=1
            
            cost1 = costs[0]+backtrack(j)

            j=idx
            while j<n and days[j]<days[idx]+7:
                j+=1
            
            cost7 = costs[1]+backtrack(j)

            j=idx
            while j<n and days[j]<days[idx]+30:
                j+=1
            
            cost30 = costs[2]+backtrack(j)

            memo[idx] = min(cost1,cost7,cost30)
            return memo[idx]
        
        return backtrack(0)
        