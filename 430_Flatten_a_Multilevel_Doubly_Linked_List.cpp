 Node* flatten(Node* head) {
    if (head)
      helper(head);
    return head;   
  }

  // Flat the list, return the tail.
  Node * helper(Node * node) {
    if (node->child) {
      Node * next = node->next;
      Node * tail = helper(node->child);
      node->next = node->child;
      node->child->prev = node;
      tail->next = next;
      node->child = 0;
      if (next) {
        next->prev = tail;
        return helper(next);
      }
      return tail;
    }
    else if (node->next)
      return helper(node->next);
    return node;
  }