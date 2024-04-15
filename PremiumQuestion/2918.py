"""
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Return the minimum number of steps needed to move the knight to the square [x, y]. It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

-300 <= x, y <= 300
0 <= |x| + |y| <= 300


"""
class Solution:
    
    from collections import deque

    def minKnightMoves(self, x: int, y: int) -> int:
        queue = deque()
        queue.append([0, 0, 0])
        visited = set([(0, 0)])
        while len(queue) > 0:
            x_loc, y_loc, n_moves = queue.popleft()
            if x_loc == x and y_loc == y:
                return n_moves
            next_loc_list = [
                (x_loc + 1, y_loc - 2),
                (x_loc + 2, y_loc - 1),
                (x_loc + 2, y_loc + 1),
                (x_loc + 1, y_loc + 2),
                (x_loc - 1, y_loc + 2),
                (x_loc - 2, y_loc + 1),
                (x_loc - 2, y_loc - 1),
                (x_loc - 1, y_loc - 2)
            ]
            for next_loc in next_loc_list:
                if next_loc not in visited:
                    queue.append(list(next_loc) + [n_moves + 1])
                    visited.add(next_loc)
        return -1

