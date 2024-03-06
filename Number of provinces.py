class UnionFind:
    def __init__(self, n):
        self.my_dict = {}
        self.provinces = n
        self.size = {}
        for i in range(n):
            self.my_dict[i] = i
            self.size[i] = 1

    def find(self, curr):
        if self.my_dict[curr] == curr:
            return curr
        self.my_dict[curr] = self.find(self.my_dict[curr])
        return self.my_dict[curr]

    def union(self, u, v):
        l, r = self.find(u), self.find(v)
        if l == r: 
            return

        self.provinces -= 1
        if self.size[l] < self.size[r]:
            self.my_dict[l] = r
            self.size[r] += self.size[l]
            return
        self.my_dict[r] = l
        self.size[l] += self.size[r]


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        union_find = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    union_find.union(i, j)

        return union_find.provinces
        
        

        

        