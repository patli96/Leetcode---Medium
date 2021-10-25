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
***Non-iterative inorder traversal***
```python
stack = []
res = []
ptr = root
while ptr or stack:
    # push all the left nodes into the stack
    while ptr:
	stack.append(ptr)
	ptr = ptr.left
    # Done searching for left children
    ptr = stack.pop()
    res.append(ptr.val)
    # Start searching for right children
    ptr = ptr.right
return res
```

For ***preorder traversal***:
```python
stack.append((GRAY, node))
stack.append((WHITE, node.right))
stack.append((WHITE, node.left))
```

For ***postorder traversal***:
```python
stack.append((WHITE, node.right))
stack.append((WHITE, node.left))
stack.append((GRAY, node))
```

### DFS

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


### BFS

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
For binary trees, a BFS could be like:
```python
class Solution:
    def bfs(k):
        # use a double-ended queue, which is more time efficient
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if (node IS TARGET) return node
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return -1
```
For some problems, you may need to track the level of trees when implementing a BFS:
```python
class Solution:
    def bfs(k):
    	# use a double-ended queue, which is more time efficient
        queue = collections.deque([root])
        # record steps
        steps = 0
        # use an array to store target nodes
        ans = []
	
        while queue:
            size = len(queue)
            # traverse all nodes in the current step
            for _ in range(size):
                node = queue.popleft()
                if (step == k) ans.append(node)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            # update step to the next by + 1
            steps += 1
        return ans
```

## Common Types of Problems

There are three commom types of problems.

**1. Search**

- Can be solved by DFS and BFS, sometimes with the help of single/ double recursions.

**2. Construct Trees**

- For example, [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) :arrow_right: [SOLUTION](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Tree/105_solution.py)

**3. Modify Trees**

## 4 Important Definitions

**1. Binary Search Tree**

- If the root has a left child, then all values in the left substree are smaller than root.val
- If the root has a right child, then all values in the right substree are greater than root.val
- No equal-values nodes
- ***Successor***:	The smallest node after the current one.
		One step right, and go left as far as you can.
- ***Predecessor***:	The largest node before the current one.
		One step left, and go right as far as you can.

**2. Complete Binary Tree**

- Give each node an index starting from 1, in this way: 
	root.index = i
	root.left.index = 2*i
	root.right.index = 2*i + 1
- Sometimes need a BFS with steps
- ***Three pointers method***

3. Path

- Single/ double recursion

4. Distance

- E.g. [863. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) :arrow_right: [SOLUTION](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Tree/863_solution.py)

## 3 Techniques

### 1. Single/Double Recursion

***Double Recursion***:
(a main DFS traversing all the nodes) + (an inner DFS doing the calculations)

```python
def dfs_inner(root):
    # If put your logic here, then it is a preorder traversal
    dfs_inner(root.left)
    dfs_inner(root.right)
    # Or if put your logic here, then it is a postorder traversal
def dfs_main(root):
    return dfs_inner(root) + dfs_main(root.left) + dfs_main(root.right)
```

### 2. Virtual Node

E.g. [814. Binary Tree Pruning](https://leetcode.com/problems/binary-tree-pruning/), [1325. Delete Leaves With a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/)

### 3. Parameter Extension

Add extra parameters to a DFS or BFS algorithm based on problems.

For example, adding a parameter to store each node's parent:
```python
def dfs(root, parent):
    if not root: return
    dfs(root.left, root)
    dfs(root.right, root)
```

Adding a parameter to store the sum of paths:
```python
def dfs(root, path_sum):
    if not root:
        # you can get the sum of path from the root to a child here
        return path_sum
    dfs(root.left, path_sum + root.val)
    dfs(root.right, path_sum + root.val)
```

Adding a parameter to store the path:
```python
def dfs(root, path):
    if not root:
        # you can get the path from the root to a child here
        return path
    path.append(root.val)
    dfs(root.left, path)
    dfs(root.right, path)
    # Undo
    path.pop()
```
