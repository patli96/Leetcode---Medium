class DisjointSet:
    father = {}

    def __init__(self, equations):
        for eq in equations:
            self.father[eq[0]] = None
            self.father[eq[3]] = None

    def find(self, x):
        ancestor = x
        while self.father[ancestor] is not None:
            ancestor = self.father[ancestor]
        while x != ancestor:
            father = self.father[x]
            self.father[x] = ancestor
            x = father
        return ancestor

    def merge(self, x, y):
        x_ancestor, y_ancestor = self.find(x), self.find(y)
        if x_ancestor != y_ancestor:
            self.father[y_ancestor] = x_ancestor

    def add(self, x):
        if x not in self.father:
            self.father[x] = None

    def if_equal(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        ds = DisjointSet(equations)

        for eq in equations:
            if eq[1] == '=':
                ds.merge(eq[0], eq[3])
        for eq in equations:
            if eq[1] == '=' and ds.if_equal(eq[0], eq[3]) is False:
                return False
            if eq[1] == '!' and ds.if_equal(eq[0], eq[3]) is True:
                return False

        return True
