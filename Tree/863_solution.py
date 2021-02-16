# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # a dictonary to store each node's parent: {node: parent_node}
    parent_dict = {}

    def traverse(self, root, parent):
        '''
        traverse the whole tree with recursion and store each node's parent node
        '''
        if root:
            Solution.parent_dict[root] = parent
            self.traverse(root.left, root)
            self.traverse(root.right, root)

    def BFS(self, node, distance, res, visited):
        '''
        recursively find the node with a distance K from the target node
        '''
        if node:
            if distance == 0:
                if node.val not in res:
                    res.append(node.val)
                    visited.append(node)
            else:
                if Solution.parent_dict[node] and Solution.parent_dict[node] not in visited:
                    visited.append(Solution.parent_dict[node])
                    self.BFS(Solution.parent_dict[node], distance - 1, res, visited)
                if node.left and node.left not in visited:
                    visited.append(node.left)
                    self.BFS(node.left, distance - 1, res, visited)
                if node.right and node.right not in visited:
                    visited.append(node.right)
                    self.BFS(node.right, distance - 1, res, visited)

    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        # traverse all the nodes and record each one's parent in a dictionary
        self.traverse(root, None)

        # implement a BFS to search all the nodes having a distance K from the target node
        res = []
        visited = [target]
        self.BFS(target, K, res, visited)

        return res