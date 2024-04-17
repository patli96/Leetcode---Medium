from collections import deque


class Node:
    def __init__(self, name: str) -> None:
        self.name = name
        self.next = set()
        self.to_value = {}


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        node_map = {}
        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]
            if x not in node_map:
                node_map[x] = Node(x)
            if y not in node_map:
                node_map[y] = Node(y)
            node_map[x].next.add(y)
            node_map[x].to_value[y] = val
            node_map[y].next.add(x)
            node_map[y].to_value[x] = 1 / val
        
        result = []
        for i in range(len(queries)):
            x, y = queries[i]
            if x not in node_map or y not in node_map:
                result.append(-1)
                continue
            queue = deque([(node_map[x], 1)])
            visited = set([x])
            found = False
            while queue:
                node, curr_val = queue.popleft()
                if y in node.next:
                    curr_val *= node.to_value[y]
                    found = True
                    break
                for next_node in node.next:
                    if next_node in visited:
                        continue
                    queue.append([node_map[next_node], curr_val * node.to_value[next_node]])
                    visited.add(next_node)
            if found is True:
                result.append(curr_val)
            else:
                result.append(-1)
        return result

