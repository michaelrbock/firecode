class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def find_nth_node_from_end(self, n):
        if not self.head: return None
        fast = self.head
        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return None
        slow = self.head
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
