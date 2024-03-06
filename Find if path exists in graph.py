class UnionFind:
    def __init__(self, n):
        self.my_dict = {}
        self.size = {}
        for i in range(n):
            self.my_dict[i] = i
            self.size[i] = 1

    def find(self, curr):
        if curr == self.my_dict[curr]:
            return curr
        self.my_dict[curr] = self.find(self.my_dict[curr])
        return self.my_dict[curr]

    def union(self, u, v):
        l, r = self.find(u), self.find(v)
        if l == r:
            return
        if self.size[l] < self.size[r]:
            self.my_dict[l] = self.my_dict[r]
            self.size[l] += self.size[r]
            return
        self.my_dict[r] = self.my_dict[l]
        self.size[r] += self.size[l]
        

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union_find = UnionFind(n)
        for u, v in edges:
            union_find.union(u, v)

        return union_find.find(source) == union_find.find(destination)