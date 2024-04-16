class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleLnkedList:

    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, new_node):
        tmp_node = self.head.next
        new_node.next = tmp_node
        new_node.prev = self.head
        self.head.next = new_node
        tmp_node.prev = new_node
    
    def remove(self, node_to_remove):
        prev_node = node_to_remove.prev
        next_node = node_to_remove.next
        prev_node.next = next_node
        next_node.prev = prev_node


class LRUCache:

    from collections import defaultdict, deque

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = DoubleLnkedList()
        self.data = {}
        
    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        node_to_update = self.data[key]
        ret_val = node_to_update.val
        del self.data[key]
        self.linked_list.remove(node_to_update)
        self.linked_list.add(node_to_update)
        self.data[key] = self.linked_list.head.next
        return ret_val
    
    def put(self, key: int, value: int) -> None:
        if key in self.data:
            node = self.data[key]
            del self.data[key]
            self.linked_list.remove(node)
        if len(self.data) == self.capacity:
            key_to_remove = self.linked_list.tail.prev.key
            del self.data[key_to_remove]
            self.linked_list.remove(self.linked_list.tail.prev)
        
        self.linked_list.add(Node(key, value))
        self.data[key] = self.linked_list.head.next



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
