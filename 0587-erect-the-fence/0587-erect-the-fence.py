class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        
        trees = sorted(trees)
        U, L = [], []
        
        def cross(A, B, C):
            x1, y1, x2, y2, x3, y3 = chain(A, B, C)
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
        
        for t in trees:
            while len(U) >= 2 and cross(t,U[-1],U[-2]) < 0:
                U.pop()
            U.append(t)
            
            while len(L) >= 2 and cross(t,L[-1],L[-2]) > 0:
                L.pop()
            L.append(t)

        return set(tuple(T) for T in (U+L))