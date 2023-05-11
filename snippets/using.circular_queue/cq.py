SIZE = 5


class CircularQueue:
    """ Circular Queue """
    items = [0, 0, 0, 0, 0]
    front = -1
    rear = -1

    def isFull(self):
        """ check if full

        Returns: true or false

        """
        if self.front == self.rear + 1 or (self.front == 0 and self.rear == SIZE - 1):
            return True
        else:
            return False

    def isEmpty(self):
        """ check if empty

        Returns: true or false

        """
        if self.front == -1:
            return True
        else:
            return False

    def enQueue(self, element: int):
        """ enqueue an element

        Args:
            element: an integer

        Returns: None

        """
        if self.isFull():
            print('Queue is full!')
            return
        else:
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % SIZE
            self.items[self.rear] = element

    def deQueue(self):
        """ dequeue an element

        Returns: an integer

        """
        if self.isEmpty():
            return -1
        else:
            element = self.items[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % SIZE

            return element

    def display(self):
        """ display the queue's elements """
        if self.isEmpty():
            print('empty queue.')
        else:
            print(f"self.front: {self.front}")
            for i in self.items:
                print(i)
            print(f"self.rear: {self.rear}")


if __name__ == "__main__":
    cq = CircularQueue()
    cq.enQueue(1)
    cq.enQueue(2)
    cq.enQueue(3)
    cq.enQueue(4)
    cq.enQueue(5)

    cq.enQueue(6)

    cq.display()
    pass
