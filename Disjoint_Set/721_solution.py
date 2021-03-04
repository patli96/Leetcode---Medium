class DisjointSet:
    def __init__(self):
        self.father = {}
        self.account = {}

    def find(self, x):
        # find ancestor
        x_ancestor = x
        while self.father[x_ancestor] is not None:
            x_ancestor = self.father[x_ancestor]
        # simplify the disjoint set
        while x != x_ancestor:
            original_father = self.father[x]
            self.father[x] = x_ancestor
            x = original_father
        return x_ancestor

    def merge(self, x, y):
        x_ancestor = self.find(x)
        y_ancestor = self.find(y)
        if x_ancestor != y_ancestor:
            self.father[y_ancestor] = x_ancestor
            self.account[x_ancestor] += self.account[y_ancestor]
            del self.account[y_ancestor]

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.account[x] = [x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        DS = DisjointSet()

        for i in range(len(accounts)):
            name, master = accounts[i][:2]
            father = accounts[i][1]
            DS.add((name, master))
            for j in range(2, len(accounts[i])):
                DS.add((name, accounts[i][j]))
                DS.merge((name, master), (name, accounts[i][j]))

        ret = []

        for key in DS.account:
            ret.append([key[0]] + sorted([x[1] for x in DS.account[key]]))

        return sorted(ret, key=lambda x: x[0])
