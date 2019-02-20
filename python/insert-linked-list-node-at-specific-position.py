class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    # Method for inserting a new node at the start of a Linked List
    def insert_at_pos(self,data,pos):
        new_node = Node()
        new_node.data = data
        if not self.head:
            self.setHead(new_node)
            return
        ptr = self.head
        for i in range(pos - 2):
           if ptr.next:
               ptr = ptr.next
        if pos == 1:
            new_node.next = ptr
            self.setHead(new_node)
        else:
            if ptr.next:
                new_node.next = ptr.next
            ptr.next = new_node
