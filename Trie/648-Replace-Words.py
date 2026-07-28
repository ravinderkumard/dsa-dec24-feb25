class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search_prefix(self,word):
        node = self.root

        prefix = []
        for ch in word:
            if ch not in node.children:
                return ""
            node = node.children[ch]
            prefix.append(ch)

            if node.is_word:
                return "".join(prefix)
        
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for root in dictionary:
            trie.insert(root)
        
        result = []

        for word in sentence.split():
            prefix = trie.search_prefix(word)
            result.append(prefix if prefix else word)
        return " ".join(result)
