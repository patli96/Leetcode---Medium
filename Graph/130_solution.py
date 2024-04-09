class Solution:

    from collections import deque

    @staticmethod
    def bfs(board, start_node, i_len, j_len):
        queue = deque()
        queue.append(start_node)
        board[start_node[0]][start_node[1]] = "#"
        while len(queue) > 0:
            node = queue.popleft()
            # check top
            if node[0] - 1 > 0 and board[node[0] - 1][node[1]] == "O":
                board[node[0] - 1][node[1]] = "#"
                queue.append((node[0] - 1, node[1]))
            # check left
            if node[1] - 1> 0 and board[node[0]][node[1] - 1] == "O":
                board[node[0]][node[1] - 1] = "#"
                queue.append((node[0], node[1] - 1))
            # check bottom
            if node[0] + 1 < i_len and board[node[0] + 1][node[1]] == "O":
                board[node[0] + 1][node[1]] = "#"
                queue.append((node[0] + 1, node[1]))
            # check right
            if node[1] + 1 < j_len and board[node[0]][node[1] + 1] == "O":
                board[node[0]][node[1] + 1] = "#"
                queue.append((node[0], node[1] + 1))
        return board

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        i_len = len(board)
        j_len = len(board[0])

        # check up border
        for j in range(j_len):
            if board[0][j] in ["X", "#"]:
                continue
            board = self.bfs(board, (0, j), i_len, j_len)
        
        # check bottom border
        for j in range(j_len):
            if board[i_len - 1][j] in ["X", "#"]:
                continue
            board = self.bfs(board, (i_len - 1, j), i_len, j_len)
        
        # check left border
        for i in range(i_len):
            if board[i][0] in ["X", "#"]:
                continue
            board = self.bfs(board, (i, 0), i_len, j_len)
        
        # check right border
        for i in range(i_len):
            if board[i][j_len - 1] in ["X", "#"]:
                continue
            board = self.bfs(board, (i, j_len - 1), i_len, j_len)

        for i in range(i_len):
            board[i] = ",".join(board[i]).replace("O", "X").replace("#", "O").split(",")

