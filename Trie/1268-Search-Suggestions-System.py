class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        prefix = ""

        for ch in searchWord:
            prefix+=ch
            idx = bisect_left(products,prefix)

            suggestions = []

            for i in range(idx,min(idx+3,len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
            
            answer.append(suggestions)
        
        return answer