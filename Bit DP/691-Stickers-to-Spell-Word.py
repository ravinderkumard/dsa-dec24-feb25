class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        full_mask = (1<<n)-1
        dp = {}
        def dfs(mask):
            if mask == full_mask:
                return 0
            
            ans = inf
            if mask in dp:
                return dp[mask]
            for sticker in stickers:
                new_mask = mask
                for ch in sticker:
                    for i in range(n):
                        if (new_mask >> i) &1:
                            continue
                        if target[i]==ch:
                            new_mask|=(1<<i)
                            break
                
                if new_mask!=mask:
                    ans = min(ans,1+dfs(new_mask))
            dp[mask] = ans
            return ans
        
        ans = dfs(0)
        return -1 if ans==inf else ans