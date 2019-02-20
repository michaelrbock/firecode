// namespace std have been included for this problem.

// Add any helper functions(if needed) above.
listNode* insert_at_tail( listNode* head, int data)
{
    if (head == NULL) {
        head = new listNode;
        head->value = data;
        return head;
    }
    listNode* curr = head;
    while (curr->next != NULL) {
        curr = curr->next;
    }
    curr->next = new listNode;
    curr->next->value = data;

    return head;
}