Node *reverse(Node *head) {
    Node *pre = NULL;
    Node *next = NULL;
    While (head) {
        next = head->next;
        head->next = pre;
        pre = head;
        head = next;
    }
}
        
