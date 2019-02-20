class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def inorder_iterative(self):
        inorder_list = []

        stack = []
        node = self
        while True:
            while node:
                stack.append(node)
                node = node.left_child
            if not stack:
                break
            node = stack.pop()
            inorder_list.append(node.get_root_val())
            node = node.right_child

        return inorder_list

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
