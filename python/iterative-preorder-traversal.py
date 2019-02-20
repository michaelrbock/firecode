class BinaryTree:

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder_iterative(self):
        pre_ordered_list = []
        stack = []
        curr = self
        while True:
            pre_ordered_list.append(curr.data)
            if curr.right_child:
                stack.append(curr.right_child)
            curr = curr.left_child
            if not curr:
                if not stack:
                    break
                curr = stack.pop()
        return pre_ordered_list

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data