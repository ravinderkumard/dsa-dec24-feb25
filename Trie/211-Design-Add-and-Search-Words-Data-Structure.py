class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.dict = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.dict
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_word = True

    def search_helper(self,word,node,idx):
        for i in range(idx,len(word)):
            ch = word[i]
            if ch=='.':
                for temp in node.children.values():
                    if self.search_helper(word,temp,i+1):
                        return True
                
                return False
            
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def search(self, word: str) -> bool:
        return self.search_helper(word,self.dict,0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)