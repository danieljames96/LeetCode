import heapq

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        hash_table = {}
        for product in products:
            for i in range(len(product)):
                hash_table.setdefault(product[:i+1], []).append(product)

        suggestions = []
        for i in range(len(searchWord)):
            searchPhrase = searchWord[:i+1]
            suggestion = hash_table.get(searchPhrase, [])
            heapq.heapify(suggestion)
            suggestions.append(heapq.nsmallest(3, suggestion))
        
        print(f'Suggestions: {suggestions}')
        return suggestions