from collections import deque


class BinaryTree:
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self,root):
        if not root: return 0
        count = 0
        to_visit = deque([root])
        while to_visit:
            curr = to_visit.popleft()
            if not curr.left_child and not curr.right_child:
                count += 1
            if curr.left_child:
                to_visit.append(curr.left_child)
            if curr.right_child:
                to_visit.append(curr.right_child)
        return count
