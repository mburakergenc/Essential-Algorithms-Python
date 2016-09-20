class Queue:
    """
    Queue Example using the power of Lists
    """
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def isEmpty(self):
        """
        Check if the Queue is empty
        :return:
        """
        return self.items == []

    def enqueue(self, item):
        """
        Add an item to the end of the Queue
        :param item:
        :return:
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove an item to the beginning of the Queue
        :return:
        """
        self.items.pop(0)

    def size(self):
        """
        Return the size of the Queue
        :return: size
        """
        return len(self.items)

    # q = Queue()
    #
    # q.enqueue("Item1")
    # q.enqueue("Item2")
    # q.enqueue("Item3")
    # q.enqueue("Item4")
    #
    # q.dequeue()
    # q.dequeue()
    #
    # print q
    #
    # print q.size()
    #
    # print q.isEmpty()
