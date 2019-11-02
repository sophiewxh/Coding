class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.maxsize = k
        self.queue = [None] * k
        # head is the index of the front, range [0, maxsize-1]
        self.head = -1
        # tail is the index of the rear, range [0, maxsize-1]
        self.tail = -1


    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            # this is the first item for an empty queue
            if self.isEmpty():
                self.head = 0
                self.tail = 0
            else:
                self.tail = (self.tail + 1) % self.maxsize
            self.queue[self.tail] = value
            return True



    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            # del self.queue[self.head]
            # there is one element left, queue is empty after deQueue
            if self.head == self.tail:
                self.head = -1
                self.tail = -1
            else:
                self.head = (self.head + 1) % self.maxsize
            return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head == -1 and self.tail == -1:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.tail + 1) % self.maxsize == self.head:
            return True
        else:
            return False

    def printCircularQueue(self):
        print(self.queue)
        print("head: " + str(self.head))
        print("tail: " + str(self.tail))

if __name__ == "__main__":
    cq = MyCircularQueue(3)

    print(cq.isEmpty())
    cq.enQueue(1)
    cq.printCircularQueue()
    print(cq.isFull())

    cq.enQueue(2)
    cq.printCircularQueue()
    print(cq.isFull())

    cq.enQueue(3)
    cq.printCircularQueue()
    print(cq.isFull())

    cq.deQueue()
    cq.printCircularQueue()
    print(cq.isFull())

    cq.deQueue()
    cq.printCircularQueue()
    print(cq.isFull())

    cq.deQueue()
    cq.printCircularQueue()
    print(cq.isEmpty())