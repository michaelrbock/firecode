class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None

    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head

    def is_list_even(self):
        if not self.head: return True
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        return length % 2 == 0
