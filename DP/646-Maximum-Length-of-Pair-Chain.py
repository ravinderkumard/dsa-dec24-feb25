class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        chain = 1

        prev = pairs[0]

        for p in pairs:
            if p[0]>prev[1]:
                chain+=1
                prev = p

        return chain