class Solution:
    def countCommas(self, n: int) -> int:
        L = []
        if n < 1000:
            return 0
        for i in range(1000,n+1):
            L.append(i)
        return len(L)        
        