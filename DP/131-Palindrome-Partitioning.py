class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        memo = {}

        def isPali(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        
        def dfs(start):
            if start==n:
                return [[]]
            
            if start in memo:
                return memo[start]
            
            result = []
            for end in range(start,n):
                if isPali(start,end):
                    current = s[start:end+1]
                    for partition in dfs(end+1):
                        result.append([current]+partition)
            memo[start] = result
            return result
        return dfs(0)