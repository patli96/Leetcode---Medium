class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        result = []
        products.sort()
        for i in range(len(searchWord)):
            result.append(
                sorted([word for word in products if word[:i + 1] == searchWord[:i + 1]])[:3]
            )
        return result
