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
        """
        node = self
        while node != None:
            node = node.next


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
        # head node is self


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def get_val(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new_node):
        self.next = new_node




if __name__ == '__main__':
    ll = MyLinkedList()
    param_1 = ll.get(3)