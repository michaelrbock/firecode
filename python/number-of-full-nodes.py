from collections import deque


class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    # Required collection modules have already been imported.
    def number_of_full_nodes(self,root):
        if not root: return 0
        full_nodes = 0
        to_visit = deque([root])
        while to_visit:
            curr = to_visit.popleft()
            if curr.left_child and curr.right_child:
                full_nodes += 1
            if curr.left_child:
                to_visit.append(curr.left_child)
            if curr.right_child:
                to_visit.append(curr.right_child)
        return full_nodes
