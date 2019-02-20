class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def find_middle_node(self):
        if not self.head: return
        # Strategy: fast & slow pointers
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow
