from collections import deque

class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node


    def validate_BST_Itr(self,root):
        # Return type should be Boolean
        # Strategy: BFS keeping track what nodes need to be > or < then.
        to_visit = deque([(root, float('-inf'), float('inf'))])  # node, gt, lt
        while to_visit:
            curr, gt, lt = to_visit.popleft()
            if curr.data < gt or curr.data > lt:
                return False
            if curr.left_child:
                to_visit.append((curr.left_child, gt, curr.data))
            if curr.right_child:
                to_visit.append((curr.right_child, curr.data, lt))
        return True
