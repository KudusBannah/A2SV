class UnionFind:
    def __init__(self):
        self.dict = {}
        self.size = {}

        for i in range(26):
            self.dict[chr(97+i)] = chr(97+i)
            self.size[chr(97+i)] = 1

    def find(self, curr):
        if self.dict[curr] == curr:
            return curr
        self.dict[curr] = self.find(self.dict[curr])
        return self.dict[curr]

    def union(self, u, v):
        l, r = self.find(u), self.find(v)
        if l == r:
            return
        if self.size[l] > self.size[r]:
            self.dict[r] = l
            self.size[l] += self.size[r]
        else:
            self.dict[l] = r
            self.size[r] += self.size[l]
                

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind()
        for equ in equations:
            u, v = equ[0], equ[-1]
            if "!" not in equ:
                union_find.union(u, v)

        for equ in equations:
            u, v = equ[0], equ[-1]
            if "!" in equ:
                if union_find.find(u) == union_find.find(v): 
                    return False
        return True