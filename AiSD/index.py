

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            x = self.head
            while x.next:
                x = x.next
            x.next = new_node
            new_node.prev = x
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None 
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_list(self):
        x = self.head
        while x:
            print(x.data)
            x = x.next

    def add_after_node(self, key, data):
        x = self.head
        while x:
            if x.next is None and x.data == key:
                self.append(data)
                return 
            elif x.data == key:
                new_node = Node(data)
                nxt = x.next
                x.next = new_node
                new_node.next = nxt
                new_node.prev = x
                nxt.prev = new_node
            x = x.next

    def add_before_node(self, key, data):
        x = self.head
        while x:
            if x.prev is None and x.data == key:
                self.prepend(data)
                return
            elif x.data == key:
                new_node = Node(data)
                prev = x.prev
                prev.next = new_node
                x.prev = new_node
                new_node.next = x
                new_node.prev = prev
            x = x.next

    def delete(self, key):
        x = self.head
        while x:
            if x.data == key and x == self.head:
                # Case 1:
                if not x.next:
                    x = None 
                    self.head = None
                    return

                else:
                    nxt = x.next
                    x.next = None 
                    nxt.prev = None
                    x = None
                    self.head = nxt
                    return 

            elif x.data == key:

                if x.next:
                    nxt = x.next 
                    prev = x.prev
                    prev.next = nxt
                    nxt.prev = prev
                    x.next = None 
                    x.prev = None
                    x = None
                    return

                else:
                    prev = x.prev 
                    prev.next = None 
                    x.prev = None 
                    x = None 
                    return 
            x = x.next

    def reverse(self):
        tmp = None
        x = self.head
        while x:
            tmp = x.prev
            x.prev = x.next
            x.next = tmp
            x = x.prev
        if tmp:
            self.head = tmp.prev


double_list = DoubleLinkedList()

double_list.append("Audi")
double_list.append("BMW")
double_list.append("Toyota")
double_list.append("Lexus")

double_list.reverse()
double_list.print_list()