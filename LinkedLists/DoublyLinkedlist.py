class Node:
    """
    Doubly Linked List Algorithms
    """
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# Create Nodes
node1 = Node("1")
node2 = Node("2")
node3 = Node("3")
node4 = Node("new node")

# Link the Nodes in both ways
node1.next = node2
node2.next = node3

node3.prev = node2
node2.prev = node1


def insertCell(afterMe, newCell):
    newCell.next = afterMe.next
    afterMe.next = newCell

    newCell.next.prev = afterMe.next
    newCell.pre = afterMe

insertCell(node2, node4)






