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

Since usually there is no cycle in a tree, a DFS could be like:
```python
function dfs(root) {
	if (some conditions）{
		// return or quit search
	}
	for (const child of root.children) {
        dfs(child)
	}
}
```

For binary trees, it could be like:
```python
function dfs(root) {
	if (some conditions）{
		// return or quit
	}
    dfs(root.left)
    dfs(root.right)
}
```
:warning: Sometimes it may require to detect cycles, a visited list may be needed.


## BFS

A common BFS algorithm of trees could be like:
```python
const visited = {}
function bfs() {
	let q = new Queue()
	q.push(INITIAL STATE)
	while(q.length) {
		let i = q.pop()
        if (visited[i]) continue
        if (i IS THE TARGET) return RESULT
		for (NODES CAN BE REACHED FROM i) {
			if (j IS VALID) {
				q.push(j)
			}
		}
    }
    return NOT FOUND
}
```
For some problems, you may need to
