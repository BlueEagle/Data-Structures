"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node  # connect the new node for the old node
            new_node.next = self.head  # connect the old node for the new node
            self.head = new_node  # move the pointer to the head onto the new node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if not self.head:
            return None
        else:
            old_head = self.head
            if self.head.next:  # there is a head and a next node
                self.head.next.prev = None
                self.head = self.head.next
                self.length -= 1
            else:  # there is no next node
                self.head = None
                self.tail = None
                self.length = 0
            return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        """
        If there are no nodes, there is nothing to hold the next or previous values. If there is no head or tail, Add the node as the current head and tail
        """
        new_tail = ListNode(value)
        if not self.head:
            self.head = new_tail
            self.tail = new_tail
            self.length += 1
        else:
            print(new_tail.value)
            old_tail = self.tail
            new_tail.prev = self.tail
            self.tail = new_tail
            self.tail.prev.next = self.tail
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        old_tail = self.tail
        if self.tail == self.head:
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
        return old_tail.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node.prev and node.next:  # They both are present
            node.prev.next = node.next
            node.next.prev = node.prev
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node
        elif not node.next:
            node.prev.next = None
            self.tail = node.prev
            self.head.prev = node
            node.next = self.head
            node.prev = None
            self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node.next and node.prev:
            node.prev.prev = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node
        elif not node.prev:
            node.next.prev = None
            self.head = node.next
            self.tail.next = node
            node.next = None
            node.prev = self.tail
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        if node.prev and node.next:  # There is a node on both sides
            node.prev.next = node.next
            node.next.prev = node.prev
            self.length -= 1
        elif not node.prev and not node.next:  # There is node surrounding node
            self.head = None
            self.tail = None
            self.length = 0
        elif not node.prev:
            self.head = node.next
            node.next.prev = None
            self.length -= 1
        elif not node.next:
            self.tail = node.prev
            node.prev.next = None
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        """
        current_max = 0
        current_node = None
        while(not current_node == self.tail):
            if not current_node:
                current_node = self.head
            if not self.head and not self.tail:
                return 0
            if self.head == current_node and self.tail == current_node:
                return current_node.value
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        return current_max
        """
        current_max = 0
        current_node = self.head
        print(f"Head: {self.head.value}")
        while(current_node.next):
            if current_node.value > current_max:
                current_max = current_node.value
            current_node = current_node.next
        return current_max
        # while(not current_node == self.tail):
        #     if not current_node:
        #         print(f"Creating node from head! {self.head.value}")
        #         current_node = self.head
        #     if not self.head and not self.tail:
        #         print("This is a 0 bro.")
        #         return 0
        #     if self.head == current_node and self.tail == current_node:
        #         print(f"Head: {self.head.value} Tail: {self.tail.value}")
        #         print(
        #             f"This is only one element, some kind of list. {current_node.value}")
        #         return current_node.value
        #     if current_node.value > current_max:
        #         print(
        #             f"{current_node.value} is greater than {current_max}. Updating current max.")
        #         current_max = current_node.value
        #     current_node = current_node.next
        # return current_max
