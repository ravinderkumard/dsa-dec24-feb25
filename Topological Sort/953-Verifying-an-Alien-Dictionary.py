class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_loc = {ch:i for i,ch in enumerate(order)}
        
        for i in range(len(words)-1):
            found_diff = False
            word1 = words[i]
            word2 = words[i+1]
            for c1,c2 in zip(word1,word2):
                if c1!=c2:
                    if order_loc[c1]>order_loc[c2]:
                        return False
                    found_diff = True
                    break
            if not found_diff and len(word1)>len(word2):
                    return False
        return True