class Solution:

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        width = max([i[0] + i[2] for i in circles])
        height = max([i[1] + i[2] for i in circles])
        n_lattice_points = 0
        for x in range(width + 1):
            for y in range(height + 1):
                if len([i for i in circles if (abs(x - i[0]) ** 2 + abs(y - i[1]) ** 2) ** 0.5 <= i[2]]) > 0:
                    n_lattice_points += 1
        return n_lattice_points

