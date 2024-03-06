class UnionFind:
    def __init__(self, n):
        self.my_dict = {}
        self.size = {}
        for i in range(n):
            self.my_dict[i+1] = i+1
            self.size[i+1] = 1

    def find(self, curr):
        if curr == self.my_dict[curr]:
            return curr
        self.my_dict[curr] = self.find(self.my_dict[curr])
        return self.my_dict[curr]

    def union(self, u, v):
        l, r = self.find(u), self.find(v)
        if l == r:
            return False
        if l > r:
            self.my_dict[r] = l
            self.size[l] += self.my_dict[r]
        else:
            self.my_dict[l] = r
            self.size[r] += self.my_dict[l]
        return True
         

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))
        for u, v in edges:
            if not union_find.union(u, v):
                break
        return [u, v]