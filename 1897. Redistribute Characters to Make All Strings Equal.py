class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}

        for word in words:
            for c in word:
                d[c] = 1 + d.get(c, 0)
        
        n = len(words)

        for val in d.values():
            if val % n != 0:
                return False
        
        return True
        