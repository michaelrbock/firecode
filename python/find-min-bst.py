class BinaryTree:

    def __init__(self, root_node = None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def find_min(self,root):
        # Return element should be of type TreeNode
        if not root: return
        curr = root
        while curr.left_child:
            curr = curr.left_child
        return curr
