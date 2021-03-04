class DisjointSet:
    def __init__(self):
        self.father = {}
        self.set_num = 0

    def merge(self, x, y):
        x_ancestor = self.find(x)
        y_ancestor = self.find(y)
        if x_ancestor != y_ancestor:
            self.father[y_ancestor] = x_ancestor
            self.set_num -= 1

    def find(self, x):
        ancestor = x

        while self.father[ancestor] is not None:
            ancestor = self.father[ancestor]

        while x != ancestor:
            father = self.father[x]
            self.father[x] = ancestor
            x = father

        return ancestor

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.set_num += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def size(self):
        return self.set_num

    def print(self):
        print(self.father)


class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n_cities = len(isConnected)

        DS = DisjointSet()

        for i in range(n_cities):
            DS.add(i)
            for j in range(n_cities):
                if j != i and isConnected[i][j] == 1:
                    DS.add(j)
                    DS.merge(i, j)

        return DS.size()

