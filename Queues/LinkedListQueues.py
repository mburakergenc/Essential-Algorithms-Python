class Node(object):
    """
    Singly Linked List Algorithms
    """
    def __init__(self, data=None, next=None, prev = None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)


# Create Nodes
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("New Cell")

# Link the Nodes
node1.next = node2
node2.next = node3


def enqueue(top, data):
    """
    Add an item using Linked Lists
    :param top:
    :param data:a
    :return:
    """
    newNode = Node()
    newNode.data = data
    newNode.next = top.next
    top.next = newNode
    newNode.prev = top

