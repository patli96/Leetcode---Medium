# Tree

## Traversal

An example of ***inorder traversal*** without recursion:
- WHITE indicates the node has not been visited
- GRAY indicates the node has already been visited
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res
```

For preorder traversal:
```python
stack.append((GRAY, node))
stack.append((WHITE, node.right))
stack.append((WHITE, node.left))
```

For postorder traversal:
```python
stack.append((WHITE, node.right))
stack.append((WHITE, node.left))
stack.append((GRAY, node))
```

## DFS

Since us
