class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n=len(words)
        def calculate(curr,prev):
            curr_word = words[curr]
            prev_word = words[prev]
            if len(curr_word)!=len(prev_word)+1:
                return False
            
            i=j=0
            while i<len(curr_word):
                if j<len(prev_word) and curr_word[i]==prev_word[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            
            return j==len(prev_word)
        
        cache = [[None]*(n+1) for _ in range(n)]

        def chain(curr,prev):
            if curr == len(words):
                return 0
            
            if cache[curr][prev+1] is not None:
                return cache[curr][prev+1]

            take = 0
            if prev==-1 or calculate(curr,prev):
                take = 1+chain(curr+1,curr)
            not_take = chain(curr+1,prev)
            cache[curr][prev+1] = max(take,not_take)
            return cache[curr][prev+1]

        return chain(0,-1)