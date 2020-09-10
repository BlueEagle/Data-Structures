class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        if not self.head:
            new_node = Node(value, None)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(value, None)
            current_head = self.head
            self.head = new_node
            self.head.next = current_head
        self.size += 1

    def add_to_tail(self, value):
        if not self.tail:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        self.size += 1

    def remove_head(self):
        if not self.head:
            return None
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            current_head = self.head
            self.head = current_head.next
            self.size -= 1
        return current_head.value

    def remove_tail(self):
        if not self.tail:
            return None
        if self.head == self.tail:
            current_tail = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
        else:
            current_tail = self.tail
            current_node = self.head
            while(current_node != None):
                if(current_node.next == self.tail):
                    self.tail = current_node
                    current_node.next = None
                current_node = current_node.next
            self.size -= 1
        return current_tail.value
