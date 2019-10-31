class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # consider head as a reference/pointer to the first node
        # in Python, the name of a variable is the reference of the object
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        The first node has index 0
        """
        if index < 0:
            return -1

        count = 0
        node = self.head
        while node:
            if count == index:
                return node.val
            node = node.next
            count += 1

        # index is larger than the number of nodes
        return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = Node(val)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        The first node has index 0
        """
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            count = 0
            node = self.head
            while node:
                if count == index-1:
                    new_node.next = node.next
                    node.next = new_node
                    break
                node = node.next
                count += 1



    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        The first node has index 0
        """
        if index == 0:
            new_head = self.head.next
            self.head = new_head
        else:
            count = 0
            node = self.head
            while node:
                if count == index - 1:
                    idx_node = node.next
                    # when index is larger than the number of existing nodes
                    if not idx_node:
                        break
                    # when index node is not the last node
                    if idx_node.next:
                        node.next = idx_node.next
                    else:
                        node.next = None
                    break
                node = node.next
                count += 1


    def printList(self):
        node = self.head
        while node:
            print(node.val)
            node = node.next


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None



if __name__ == '__main__':
    ll = MyLinkedList()
    ll.addAtHead(2)
    ll.deleteAtIndex(1)
    ll.printList()
